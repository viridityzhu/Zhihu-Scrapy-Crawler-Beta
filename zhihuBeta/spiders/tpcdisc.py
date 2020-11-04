# -*- coding: utf-8 -*-
import scrapy
from zhihuBeta.items import ZhihubetaItem
import json


class ZhtdSpider(scrapy.Spider):
    name = 'zhtd'
    allowed_domains = ['zhihu.com']
    # 专业：口腔医学 19589126 妇产科学 21199525 内科学 19628411
    # 非专业：养生 19555542 ，生活习惯 19557781 ，健康常识 19651260
    topicId = '19651260'  # 医学互联网
    # topic follower
    start_urls = ['https://www.zhihu.com/api/v4/topics/' +
                  topicId + '/feeds/top_activity?include=data[*].target.author%3Bdata[*].target.question.author&limit=10']

    def parse(self, response):
        json_data = json.loads(response.body)['data']
        topicId = response.url.split('/')[6]
        # ----------获取话题follower的url以及其他信息---------
        for i in json_data:
            item = ZhihubetaItem()
            if i['target']['type'] in ('article', 'question'):
                item['url_token'] = i['target']['author']['url_token']
            elif i['target']['type'] == 'answer':
                item['url_token'] = i['target']['author']['url_token']
                # question author
                qitem = ZhihubetaItem()
                qitem['url_token'] = i['target'][
                    'question']['author']['url_token']
                if qitem['url_token'] != '':
                    yield qitem

            if item['url_token'] != '':
                yield item
        # -------------判断翻页------------------
        # isEnd表明是否已加载到最后一页
        isEnd = json.loads(response.body)['paging']['is_end']
        # 不到最后一页就翻页
        if not isEnd:
            # self.offset[0] += 20
            nextUrl = json.loads(response.body)['paging']['next']
            yield scrapy.Request(nextUrl, callback=self.parse)
        # else:
        #     self.logger.info('isEnd:' + str(isEnd))
