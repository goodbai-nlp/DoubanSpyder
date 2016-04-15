#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: xfbai
@contact: muyeby@gmail.com
@site: muyeby.github.io
@software: PyCharm
@file: spider.py
@time: 16-3-21 下午3:36
"""
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from Douban.items import DoubanItem
from scrapy.contrib.loader import ItemLoader, Identity
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class DoubanSpyder(BaseSpider):
    name = 'douban'
    allowed_domains = ["movie.douban.com"]
    start_urls = []

    def start_requests(self):
        file_opened = open('movie_name.txt','r')
        try:
            url_head = "http://movie.douban.com/subject_search?search_text="
            for line in file_opened:
                self.start_urls.append(url_head+line+"&cat=1002")
            for url in self.start_urls:
                yield Request(url,callback=self.parse,cookies=[{'name': 'COOKIE_NAME','value': 'VALUE','domain': '.douban.com','path': '/'},])
        finally:
            file_opened.close()

    def parse(self,response):
        hxs = Selector(response)
        tmp_keyword = hxs.xpath('//div[@class="mb40"]/div/p/a/text()').extract()
        tmp = str(tmp_keyword[0]).split(' ')
        keyword = tmp[1]
        movie_link = hxs.xpath('//*[@id="content"]/div/div/div/table/tr/td/a/@href').extract()
        for item in movie_link:
            yield Request(item,meta={'keyword': keyword},callback=self.parse_article,cookies=[{'name': 'COOKIE_NAME','value': 'VALUE','domain': '.douban.com','path': '/'},])

    def parse_article(self,response):
        hxs = Selector(response)
        keyword = response.meta['keyword']
        movie_name = hxs.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        movie_roles_paths = hxs.xpath('//*[@id="info"]/span[3]/span[2]')
        movie_roles = []
        for movie_roles_path in movie_roles_paths:
            movie_roles = movie_roles_path.select('.//*[@rel="v:starring"]/text()').extract()
        movie_classification= hxs.xpath('//span[@property="v:genre"]/text()').extract()
        douban_item = DoubanItem()
        douban_item['movie_keyword'] = keyword
        douban_item['movie_name'] = ''.join(movie_name).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';').replace(' ','')
        douban_item['movie_roles'] = ';'.join(movie_roles).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
        douban_item['movie_classification'] = ';'.join(movie_classification).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
        article_link = hxs.xpath('//*[@id="review_section"]/div/div/div/h3/a/@href').extract()
        tmp = "https://movie.douban.com/review/"
        for item in article_link:
            if tmp in item:
                yield Request(item,meta={'item': douban_item},callback=self.parse_item,cookies=[{'name': 'COOKIE_NAME','value': 'VALUE','domain': '.douban.com','path': '/'},])

    def parse_item(self,response):
        hxs = Selector(response)
        item = response.meta['item']
        comment_title = hxs.xpath('//span[@property="v:summary"]/text()').extract()
        comment_detail = hxs.xpath('//*[@property="v:description"]/text()').extract()
        item['comment_title'] = ''.join(comment_title).strip().replace(',',';').replace('\'','\\\'')
        tmp= '\n'.join(comment_detail).strip().replace(',',';').replace('\'','\\\'')
        item['comment_detail'] = tmp.split('\n')
        yield item
