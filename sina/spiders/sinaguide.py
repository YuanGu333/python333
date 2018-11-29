# -*- coding: utf-8 -*-
import scrapy
import os
from sina.items import SinaItem
from scrapy_redis.spiders import RedisSpider

#class SinaguideSpider(scrapy.Spider):
class SinaguideSpider(RedisSpider):
    name = 'sinaguide'
    # redis中的键
    redis_key = 'sinaguidespider:start_urls'
    #allowed_domains = ['sina.com.cn']
    #start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        # 获取大类的标题和链接
        parentTitles = response.xpath('//div[@class="clearfix"]/h3[@class="tit02"]/a/text()').extract()
        parentUrls = response.xpath('//div[@class="clearfix"]/h3[@class="tit02"]/a/@href').extract()
        
        # 获取小类的标题和链接
        subTitles = response.xpath('//div[@class="clearfix"]/ul[@class="list01"]/li/a/text()').extract()
        subUrls = response.xpath('//div[@class="clearfix"]/ul[@class="list01"]/li/a/@href').extract()
        
        # 遍历每个大类
        for i in range(len(parentTitles)):
            #print(parentTitle)
            # 父目录的路径
            parentFilename = './Data/' + parentTitles[i]
            
            # 如果父目录路径不存在 则创建
            #if not os.path.exists(parentFilename):
            #    os.makedirs(parentFilename)
            
            # 爬取所有的小类
            for j in range(0, len(subTitles)):
                if_belong = subUrls[j].startswith(parentUrls[i])
                # 只有该小类是属于当前的大类的情况下 才把小类放到大类的目录下
                if if_belong:
                    #print(parentUrls[i], '---', subUrls[j])
                    #subFilename = parentFilename + '/' + subTitles[j]
                    #print(subFilename)
                    # 如果子目录不存在 则创建
                    #if not os.path.exists(subFilename):
                    #    os.makedirs(subFilename)
                
                    # 创建item对象 描述每一个小类链接
                    item = SinaItem()
                    item['parentTitle'] = parentTitles[i]
                    item['parentUrls'] = parentUrls[i]
                    item['subTitle'] = subTitles[j]
                    item['subUrls'] = subUrls[j]
                    #item['subFilename'] = subFilename # 唯一
                    # 把item对象添加到items数组中
                    items.append(item)
        #print(len(items)) # 217   
        for item in items:
            #print(item)
            # 给小类url发送请求 meta表示要额外传递的参数
            # 参数 url 发送新的请求的url链接
            # 参数callback Scrapy框架发送新的请求后 回到Spiders模块后触发的方法
            # 参数meta 额外传递的数据
            yield scrapy.Request(url = item['subUrls'], callback = self.second_parse, meta = {'meta_1': item})
        
        
    # 对于返回的小类的url 再进行递归请求
    def second_parse(self, response):
        #print('response:', response)
        #print('response meta:', response.meta['meta_1'])
        
        # 提取meta数据
        meta_1 = response.meta['meta_1']
        
        # 取出小类中帖子的链接
        sonUrls = response.xpath('//a/@href').extract()

        items = []
        for i in range(len(sonUrls)):
            # 检查是否以大类链接开头
            if_belong = sonUrls[i].startswith(meta_1['parentUrls']) and sonUrls[i].endswith('.shtml')
            
            # 如果属于本大类的帖子链接 才需要提取出来
            if if_belong:
                #print(sonUrls[i])
                    # 创建item对象 描述每一个帖子的链接
                    item = SinaItem()
                    item['parentTitle'] = meta_1['parentTitle']
                    item['parentUrls'] = meta_1['parentUrls']
                    item['subTitle'] = meta_1['subTitle']
                    item['subUrls'] = meta_1['subUrls']
                    #item['subFilename'] = meta_1['subFilename']
                    item['sonUrls'] = sonUrls[i] # 唯一
                    items.append(item)

        #print(len(items)) # 
        for item in items:
            yield scrapy.Request(url = item['sonUrls'], callback = self.detail_parse, meta = {'meta_2': item})

    # 对于返回的帖子的url 再进行递归请求
    def detail_parse(self, response):
        #print('response:', response)
        #print('response meta:', response.meta['meta_2'])
        
        # 提取meta数据
        meta_2 = response.meta['meta_2']
        
        head = response.xpath('//h1[@id="artibodyTitle"]/text() | //h1[@class="main-title"]/text()').extract()
        if len(head) > 0:
            head = head[0]
        else:
            head = ''
        content_list = response.xpath('//div[@id="artibody"]/p/text()').extract()
        
        #print('head:', head)
        #print('content_list:', content_list)
        content = ''
        for content_one in content_list:
            content += content_one

        item = SinaItem()
        item['parentTitle'] = meta_2['parentTitle']
        item['parentUrls'] = meta_2['parentUrls']
        item['subTitle'] = meta_2['subTitle']
        item['subUrls'] = meta_2['subUrls']
        #item['subFilename'] = meta_2['subFilename']
        item['sonUrls'] = meta_2['sonUrls']
        item['head'] = head
        item['content'] = content
        
        yield item


