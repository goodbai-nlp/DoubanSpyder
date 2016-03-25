# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.exporters import XmlItemExporter
import json
import codecs
import Write as W
import os
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class DoubanPipeline(object):
    # def __init__(self):
    #     self.files = {}
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #      pipeline = cls()
    #      crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    #      crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    #      return pipeline
    #
    # def spider_opened(self, spider):
    #     file = open('%s_products.xml' % spider.name, 'w+b')
    #     self.files[spider] = file
    #     self.exporter = XmlItemExporter(file)
    #     self.exporter.start_exporting()
    #
    # def spider_closed(self, spider):
    #     self.exporter.finish_exporting()
    #     file = self.files.pop(spider)
    #     file.close()
    #
    # def process_item(self, item, spider):
    #     self.exporter.export_item(item)
    #     return item
    def __init__(self):
        #self.file = codecs.open('data.dat',mode='wb',encoding='utf-8')
        self.path = os.getcwd()+'/spider_products'
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        w=W.Write(item,self.path)
        w.run()
        #tmp = self.path +'/%s'%item['movie_keyword']
        #if not os.path.isdir(tmp):
            #os.mkdir(tmp)
        #tmp=tmp+ u'/%s'%item['movie_name']
        #if not os.path.isdir(tmp):
            #os.mkdir(tmp)
        #my_file = codecs.open('%s/%s.xml' % (tmp,item['comment_title']),mode='wb',encoding='utf-8')
        #line = json.dumps(dict(item))+'\n'
        #my_file.write(line.decode("unicode_escape"))
        return item
