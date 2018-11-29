# -*- coding: utf-8 -*-
import scrapy
from magespider.items import MagespiderItem


class MspiderSpider(scrapy.Spider):
    name = 'mspider'
    allowed_domains = ['python.tedu.cn/']
    start_urls = ['http://python.tedu.cn/']

    # 重写父类的parse方法 接收响应
    def parse(self, response):
        # 获取所有爬的列表
        need_list = response.xpath('//div[@class="backg"]//div[@class="main"]')
        # 遍历每个城市
        phone_list = []
        dizhi_list = []
        jj = {}
        alist = []
        for each in need_list:
            # 提取城市
            item = MagespiderItem()

            name = each.xpath('//div[@class="backg"]//div[@class="container clearfix"]//a/text()').extract()
            # print(len(name))
            # print(name)
            item['name'] = name

            phone = each.xpath('//div[@class="backg"]//div[@class="container clearfix"]//span/text()').extract()
            for i in range(len(phone)):
                # 判断奇偶，来插入数据
                if i%2==0:
                    phone_list.append(phone[i])
                else:
                    dizhi_list.append(phone[i])
                    if i ==67:
                        break
            item['phone'] = phone_list
            item['info'] = dizhi_list
            # jj = dict(zip(phone_list,dizhi_list))
            # print(jj)
            alist.append(item)
            print(alist)
        yield alist


