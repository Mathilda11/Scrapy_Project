# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
        # 排名
        title = scrapy.Field()
        bd = scrapy.Field()
        star = scrapy.Field()
        quote = scrapy.Field()
        # 电影名称
        # 评分
        # 评论人数

