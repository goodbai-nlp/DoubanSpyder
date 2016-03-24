# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_keyword = scrapy.Field()
    movie_name = scrapy.Field()
    movie_roles = scrapy.Field()
    movie_classification = scrapy.Field()
    comment_title = scrapy.Field()
    comment_detail = scrapy.Field()
