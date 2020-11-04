# -*- coding: utf-8 -*-
import scrapy
from zhihuBeta.items import ZhihubetaItem
import json


class ZhtfSpider(scrapy.Spider):
    name = 'zhtf'
    allowed_domains = ['zhihu.com']
    topicId = '19651260'  # 医学互联网
    # topic follower
    start_urls = ['https://www.zhihu.com/api/v4/topics/' +
                  topicId + '/followers?limit=50&offset=0']

    def parse(self, response):
        json_data = json.loads(response.body)['data']
        topicId = response.url.split('/')[6]
        # ----------获取话题follower的url以及其他信息---------
        for i in json_data:
            item = ZhihubetaItem()
            item['url_token'] = i['url_token']
            if item['url_token'] != '':
                yield item
        # -------------判断翻页------------------
        # isEnd表明是否已加载到最后一页
        isEnd = json.loads(response.body)['paging']['is_end']
        # 不到最后一页就翻页
        if not isEnd:
            # self.offset[0] += 20
            yield scrapy.Request('https://www.zhihu.com/api/v4/topics/' + topicId + '/followers?limit=50&offset=' + str(int(response.url.split('=')[-1]) + 50), callback=self.parse)
        # else:
        #     self.logger.info('isEnd:' + str(isEnd))
