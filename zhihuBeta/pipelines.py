import csv
from zhihuBeta.items import ZhihubetaItem, UserFolloweeItem, UserFollowerItem, UserinformationItem
import os
import time


class writeCSVof1Pipeline(object):

    def __init__(self):
        self.count = 0
        self.start = time.time()
        if not os.path.isfile("./data/userInfo.csv"):
            writer = csv.writer(open('./data/userInfo.csv', 'a+'),
                                lineterminator='\n')
            item = UserinformationItem()
            writer.writerow([key for key in item.fields.keys()])

    def process_item(self, item, spider):
        self.count += 1
        cur = time.time()
        T = int(cur - self.start)
        if self.count % 10 == 0:
            print("item count: " + str(self.count) + "      time:" + str(int(T / 3600)
                                                                         ) + "h " + str(int(T / 60) % 60) + "m " + str(T % 60) + "s......")
        if isinstance(item, ZhihubetaItem):
            writer = csv.writer(open('./data/url_token.csv', 'a+'),
                                lineterminator='\n')
            writer.writerow([item[key] for key in item.keys()])

            return item
        elif isinstance(item, UserFolloweeItem):
            writer = csv.writer(open('./data/userFollowee.csv', 'a+'),
                                lineterminator='\n')
            writer.writerow([item[key] for key in item.keys()])
            writer = csv.writer(open('./tempData/finishedUe.csv', 'a+'),
                                lineterminator='\n')
            writer.writerow([item['url_token_level1']])
            return item
        elif isinstance(item, UserFollowerItem):
            writer = csv.writer(open('./data/userFollower.csv', 'a+'),
                                lineterminator='\n')
            writer.writerow([item[key] for key in item.keys()])
            writer = csv.writer(open('./tempData/finishedUr.csv', 'a+'),
                                lineterminator='\n')
            writer.writerow([item['url_token_level1']])
            return item
        elif isinstance(item, UserinformationItem):
            writer = csv.writer(open('./data/userInfo.csv', 'a+'),
                                lineterminator='\n')
            # writer.writerow([key for key in item.keys()])
            writer.writerow([item[key] for key in item.keys()])
            # writer = csv.writer(open('./tempData/finishedUinfo.csv', 'a+'),
            #                     lineterminator='\n')
            # writer.writerow([item['url_token']])
            return item
