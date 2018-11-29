# -*- coding: utf-8 -*-
import scrapy
from magespider.items import MeinvItem
from urllib import request
from base64 import *
import re
# js渲染解密还是没弄懂，先做下别的爬虫
class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['jandan.net']
    url ='http://jandan.net/ooxx/page-'
    offset = 1
    start_urls = [url+str(offset)]

    # 重写父类的parse方法 接收响应
    def parse(self, response):
        # 获取所有爬的列表
        need_list = response.xpath('//ol[@class="commentlist"]//li//div[@class="text"]//p/img').extract()
        # 遍历每个城市
        for each in need_list:

            # 声明一下item是来自于MeinvTtem的
            item = MeinvItem()
            # 作者
            # name = each.xpath('//ol[@class="commentlist"]//li//strong/text()').extract()
            # # print(len(name))
            # # print(name)
            # item['name'] = name
            # time = each.xpath('//ol[@class="commentlist"]//li//small/text()').extract()
            # item['time'] = time
            # # 点赞数
            # good = each.xpath('//ol[@class="commentlist"]//li//div[@class="jandan-vote"]//span[2]/text()').extract()
            # item['good'] = good
            # # 反对数和吐槽数
            # bad = each.xpath('//ol[@class="commentlist"]//li//div[@class="jandan-vote"]//span[3]/text()').extract()
            # item['bad'] = bad
            # # 贴子号
            # num = each.xpath('//ol[@class="commentlist"]//li//div[@class="text"]//span/text()').extract()
            # item['num'] = num
            # 图片地址
            # img = each.xpath('//ol[@class="commentlist"]//li//div[@class="text"]//p/img').extract()
            m = each.encode('utf-8')
            m = b64decode(m)
            item["img"] = "http:"+str(m,encoding='utf-8')
            item["img"] = item["img"].replace('mw600','large')
            print(item["img"])     
            yield item
            # if self.offset <= 38:
            #     self.offset+=1
            # yield scrapy.Request(self.url+str(self.offset),callback=self.parse)


        # if xia:
        #     yield scrapy.Request(url = xia[0],callback=self.parse)