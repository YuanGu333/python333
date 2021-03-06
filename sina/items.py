# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # 大类的标题
    parentTitle = scrapy.Field()
    # 大类的链接
    parentUrls = scrapy.Field()

    # 小类的标题
    subTitle = scrapy.Field()
    # 小类的链接
    subUrls = scrapy.Field()
    
    # 小类目录存放路径
    #subFilename = scrapy.Field()

    # 帖子的链接
    sonUrls = scrapy.Field()
    # 帖子的标题
    head = scrapy.Field()
    # 帖子的内容
    content = scrapy.Field()
