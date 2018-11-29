# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 在这里写需要爬取的字段
    # 地区名
    # //div[@class="backg"]//div[@class="container clearfix"]//a
    name = scrapy.Field()
    # 电话号码
    phone = scrapy.Field()
    # //div[@class="backg"]//div[@class="container clearfix"]//span
    # 地址
    info = scrapy.Field()
class MeinvItem(scrapy.Item):
    # 作者
    name = scrapy.Field()
    # 发布时间
    time = scrapy.Field()
    # 点赞数
    good = scrapy.Field()
    # 反对数和吐槽数
    bad = scrapy.Field()
    # 贴子号
    num = scrapy.Field()
    # 图片地址
    img = scrapy.Field()
class ZuFangItem(scrapy.Item):
    # 标题
    biaoti = scrapy.Field()
    # 链接
    lian = scrapy.Field()
    # 位置
    weizhi = scrapy.Field()
    # 平方
    pingf = scrapy.Field()

