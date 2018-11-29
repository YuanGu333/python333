# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MagespiderPipeline(object):
    def __init__(self):
        self.filename = open('teacher.json','w',encoding = 'utf-8')
    def process_item(self, item, spider):
        json_str = json.dumps(dict(item)) + '\n'
        self.filename.write(str(json_str.encode('utf-8'),encoding='utf-8'))
        return item
    def close_spider(self,spider):
        self.filename.close()
class MeinvPipeline(object):
    def __init__(self):
        self.filename = open('meinv.json','w',encoding = 'utf-8')
    def process_item(self, item, spider):
        json_str = json.dumps(dict(item)) + '\n'
        self.filename.write(str(json_str.encode('utf-8'),encoding='utf-8'))
        return item
    def close_spider(self,spider):
        self.filename.close()
class ZuFangPipeline(object):
    def __init__(self):
        self.filename = open('ZuFang.json','w',encoding = 'utf-8')
    def process_item(self, item, spider):
        json_str = json.dumps(dict(item)) + '\n'
        self.filename.write(str(json_str.encode('utf-8'),encoding='utf-8'))
        return item
    def close_spider(self,spider):
        self.filename.close()
