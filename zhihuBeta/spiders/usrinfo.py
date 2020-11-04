# -*- coding: utf-8 -*-
import scrapy
from zhihuBeta.items import UserinformationItem
import json
import csv
import os
import time


class ZhuiSpider(scrapy.Spider):
    '''user info'''
    name = 'zhui'
    allowed_domains = ['zhihu.com']
    topicId = '19873682'  # 医学互联网

    # 取任务
    def start_requests(self):
        userListF = []
        finishedUe = []
        self.start = time.time()
        print("开始取任务-----------")
        self.urlUnit = ['https://www.zhihu.com/api/v4/members/',
                        '?include=data[*].gender,voteup_count,thanked_count,follower_count,following_count,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,columns_count,favorite_count,favorited_count,logs_count,included_answers_count,included_articles_count,included_text,message_thread_token,is_active,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,hosted_live_count,participated_live_count,allow_message']
        try:
            with open('./data/url_token.csv', 'r+') as f:
                reader = csv.reader(f)
                for im in reader:
                    userListF.append(im[0])
        except FileNotFoundError:
            self.logger.info("No url_token tasks.")
        cur = time.time()
        T = int(cur - self.start)
        print("完成url_token    time:" + str(int(T / 3600)) + "h " +
              str(int(T / 60) % 60) + "m " + str(T % 60) + "s......")

        try:
            with open('./data/userFollowee.csv', 'r+') as f:
                reader = csv.reader(f)
                for im in reader:
                    userListF.append(im[1])
        except FileNotFoundError:
            self.logger.info("No user followee tasks.")
        cur = time.time()
        T = int(cur - self.start)
        print("完成ee    time:" + str(int(T / 3600)) + "h " +
              str(int(T / 60) % 60) + "m " + str(T % 60) + "s......")

        try:
            with open('./data/userFollower.csv', 'r+') as f:
                reader = csv.reader(f)
                for im in reader:
                    userListF.append(im[1])
        except FileNotFoundError:
            self.logger.info("No user follower tasks.")
        cur = time.time()
        T = int(cur - self.start)
        print("完成er    time:" + str(int(T / 3600)) + "h " +
              str(int(T / 60) % 60) + "m " + str(T % 60) + "s......")

        try:
            with open('./tempData/finishedUinfo.csv', 'r+') as f:
                reader = csv.reader(f)
                for im in reader:
                    finishedUe.append(im[0])
        except FileNotFoundError:
            open('./tempData/finishedUinfo.csv', 'w+')
        except:
            pass
        cur = time.time()
        T = int(cur - self.start)
        print("完成finishedInfo    time:" + str(int(T / 3600)) + "h " +
              str(int(T / 60) % 60) + "m " + str(T % 60) + "s......")

        userListF = list(set(userListF))
        setF = set(finishedUe)
        self.userList = [
            item for item in userListF if item not in setF]
        self.userList = self.userList[:50000]  # 5000改成50000好了
        reqs = []
        cur = time.time()
        T = int(cur - self.start)
        print("got new task:" + str(len(self.userList)) + "    time:" + str(int(T / 3600)) + "h " +
              str(int(T / 60) % 60) + "m " + str(T % 60) + "s......")

        for i in self.userList:  # 每次取5000个任务，避免占太多内存
            req = scrapy.Request(self.urlUnit[0] + i + self.urlUnit[1])
            reqs.append(req)
        return reqs

    def parse(self, response):
        json_data = json.loads(response.body)
        u = response.url.split('/')[6].split('?')[0]
        item = UserinformationItem()
        for field in item.fields:
            if field in json_data.keys():
                try:
                    item[field] = json_data.get(field)
                except:
                    item[field] = ''
            # if field == "followee_count":
            #     item[field] = json_data.get('following_count')

        # self.userList.remove(u)

        # if user task finished, then add new ones:
        if len(self.userList) < 1:
            self.logger.info('task over. trying to fetch new ones...')
            userListF = []
            finishedUe = []
            try:
                with open('./data/url_token.csv', 'r') as f:
                    reader = csv.reader(f)
                    for im in reader:
                        userListF.append(im[0])
            except:
                pass
            try:
                with open('./data/userFollowee.csv', 'r') as f:
                    reader = csv.reader(f)
                    for im in reader:
                        userListF.append(im[1])
            except:
                pass
            try:
                with open('./data/userFollower.csv', 'r') as f:
                    reader = csv.reader(f)
                    for im in reader:
                        userListF.append(im[1])
            except:
                pass

            with open('./tempData/finishedUinfo.csv', 'r') as f:
                reader = csv.reader(f)
                for im in reader:
                    finishedUe.append(im[0])
            userListF = list(set(userListF))
            setF = set(finishedUe)
            self.userList = [
                item for item in userListF if item not in setF]

            self.userList = self.userList[:50000]
            copyList = self.userList.copy()
            cur = time.time()
            T = int(cur - self.start)
            print("got new task:" + str(len(self.userList)) + "    time:" + str(int(T / 3600)) + "h " +
                  str(int(T / 60) % 60) + "m " + str(T % 60) + "s......")
            for i in copyList:  # 每次取5000个任务，避免占太多内存
                req = scrapy.Request(
                    self.urlUnit[0] + i + self.urlUnit[1])
                # self.logger.info('new req:{}'.format(i))
                yield req

        yield item
