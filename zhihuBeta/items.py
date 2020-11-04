# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihubetaItem(scrapy.Item):
    url_token = scrapy.Field()


class UserFolloweeItem(scrapy.Item):
    url_token_level1 = scrapy.Field()
    url_token_level2 = scrapy.Field()


class UserFollowerItem(scrapy.Item):
    url_token_level1 = scrapy.Field()
    url_token_level2 = scrapy.Field()


class UserinformationItem(scrapy.Item):
    # userID---唯一标识
    url_token = scrapy.Field()
    # 昵称
    name = scrapy.Field()
    # 回答数
    answer_count = scrapy.Field()
    # 提问数
    question_count = scrapy.Field()
    # 文章数
    articles_count = scrapy.Field()
    # 专栏数
    columns_count = scrapy.Field()
    # 粉丝数
    follower_count = scrapy.Field()
    # 关注者数
    following_count = scrapy.Field()
    # 收藏数
    favorite_count = scrapy.Field()
    # 被收藏数
    favorited_count = scrapy.Field()
    # 想法数
    pins_count = scrapy.Field()
    # 公共编辑数
    logs_count = scrapy.Field()
    # 获得赞数
    voteup_count = scrapy.Field()
    # 获得感谢数
    thanked_count = scrapy.Field()
    # 开设live数
    hosted_live_count = scrapy.Field()
    # 参与live数
    participated_live_count = scrapy.Field()
    # 关注专栏数
    following_columns_count = scrapy.Field()
    # 关注话题数
    following_topic_count = scrapy.Field()
    # 关注问题数
    following_question_count = scrapy.Field()
    # 关注收藏夹数
    following_favlists_count = scrapy.Field()
    # 性别
    gender = scrapy.Field()
    # 是否活跃
    is_active = scrapy.Field()
