# -*- coding: utf-8 -*-
import scrapy
from zhihuBeta.items import UserFollowerItem
import json
import csv
import os
import math


class ZhufrSpider(scrapy.Spider):
    '''user follower'''
    name = 'zhufr'
    allowed_domains = ['zhihu.com']
    topicId = '19873682'  # 医学互联网

    # 从level1user-finisheduser中取任务
    def start_requests(self):
        userListF = []
        finishedUe = []
        u403 = {}

        self.urlUnit = ['https://www.zhihu.com/api/v4/members/',
                        '/followers?limit=20&offset=']
        with open('./data/url_token.csv', 'r+') as f:
            reader = csv.reader(f)
            for im in reader:

                userListF.append(im[0])

        try:
            with open('./tempData/ReallyFinishedUr.csv', 'r+') as f:
                reader = csv.reader(f)
                for im in reader:
                    if im[1] == 'E:403':
                        u403[im[0]] = im[2]  # 'url-token':pageNum
                    if im[1] == 'FinE:403':
                        # 如果有已完成的403（一定在未完成的后面），把任务再去掉
                        u403.pop(im[0])
                    finishedUe.append(im[0])
        except FileNotFoundError:
            open('./tempData/ReallyFinishedUr.csv', 'w+')
        self.userList = [
            item for item in userListF if item not in set(finishedUe)]

        reqs = []
        # 403任务放进待爬列表里
        for i in u403.keys():
            req = scrapy.Request(
                self.urlUnit[0] + i + self.urlUnit[1] + str(u403[i]))
            reqs.append(req)
        # 403任务写进已完成里
        for i in u403.keys():
            with open('./tempData/ReallyFinishedUr.csv', 'a+') as f:
                writer = csv.writer(f)
                writer.writerow([i, 'FinE:403', 'Non'])

        for i in self.userList:
            req = scrapy.Request(self.urlUnit[0] + i + self.urlUnit[1] + '0')
            reqs.append(req)
        self.logger.warning("New task num: {}".format(
            len(set(reqs))))
        return reqs

    def parse(self, response):
        json_data = json.loads(response.body)['data']
        u1 = response.url.split('/')[6]

        totals = json.loads(response.body)['paging']['totals']
        # 大V抽取
        # 大于10万的抽1000（1%），1~10万抽（3%），5000~1万（10%）
        pageToTurn = 1  # 默认翻1页 乘在index后面
        if totals > 100000:
            pageToTurn = (totals // 20 + 1) // 100 + 1
        elif totals > 10000:
            pageToTurn = ((totals // 20 + 1) // 100 + 1) * 3
        elif totals > 5000:
            pageToTurn = (totals // 20 + 1) // 10 + 1
        # ----------获取user follower的url以及其他信息---------
        # 拿出urltoken，和一级用户token放在一起
        for i in json_data:
            item = UserFollowerItem()
            item['url_token_level1'] = u1
            item['url_token_level2'] = i['url_token']
            if item['url_token_level2'] != '':
                yield item

        # 把已完成的task写到csv(pipeline)
        # -------------判断翻页------------------
        # 大V有可能翻页超过总页数……
        if pageToTurn > 1:  # 是大V
            nextPage = int(response.url.split('=')[-1]) + 20 * pageToTurn
            totalPage = math.ceil(totals / 20)
            if nextPage > totalPage:
                isEnd = True
        # isEnd表明是否已加载到最后一页
        isEnd = json.loads(response.body)['paging']['is_end']
        # 不到最后一页就翻页
        if not isEnd:
            # self.offset[0] += 20
            yield scrapy.Request(self.urlUnit[0] + u1 + self.urlUnit[1] + str(int(response.url.split('=')[-1]) + 20 * pageToTurn), callback=self.parse)
        else:
            # 判断有没有数完所有人
            fList = []
            with open('./tempData/finishedUr.csv', 'r+') as f:
                reader = csv.reader(f)
                for im in reader:
                    fList.append(im[0])
            count = fList.count(u1)
            self.logger.info(
                'user:{}, total:{}, got:{}'.format(u1, totals, count))
            with open('./tempData/ReallyFinishedUr.csv', 'a+') as f:
                writer = csv.writer(f)
                writer.writerow([u1, totals, count])
