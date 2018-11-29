# -*- coding: utf-8 -*-
import scrapy
from magespider.items import ZuFangItem
# 开始爬取租房信息，不太多，500条就好了，怕被抓~~
# 成功爬取了38页数据~~
class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['cs.lianjia.com']
    url ='http://cs.lianjia.com/zufang/pg'
    offset = 2
    start_urls = [url+str(offset)]


    def parse(self, response):
        list = response.xpath('//ul[@id ="house-lst"]')


        for each in list:
            item = ZuFangItem()

            biaoti=each.xpath('//div[@class="info-panel"]//h2/a/text()').extract(),
            item['biaoti']=biaoti
            lian=each.xpath('//div[@class="info-panel"]//h2/a/@href').extract(),
            item['lian']=lian
            pingf=each.xpath('//div[@class="info-panel"]//span/text()').extract(),
            item['pingf']=pingf
            weizhi=each.xpath('//div[@class="con"]/text()').extract()
            item['weizhi']=weizhi
        yield item
        if self.offset <= 38:
            self.offset+=1
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)


        