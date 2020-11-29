# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GushiwenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ShijingScanItem(scrapy.Item):
    chapterRef=scrapy.Field()
    nameli=scrapy.Field()
    linkli=scrapy.Field()
class ShijingSingleItem(scrapy.Item):
    title=scrapy.Field()
    pageLink=scrapy.Field()
    yuanWen=scrapy.Field()
    zhuYiShang=scrapy.Field()
class YemengdeItem(scrapy.Item):
    title=scrapy.Field()
    author=scrapy.Field()
    yuanWen=scrapy.Field()
    shangXi=scrapy.Field()
    pagelink=scrapy.Field()
class ShiciByAuthorItem(scrapy.Item):
    title=scrapy.Field()
    author=scrapy.Field()
    yuanWen=scrapy.Field()
    shangXi=scrapy.Field()
    pagelink=scrapy.Field()
# class ShiciByMarkItem(scrapy.Item):
    # title=scrapy.Field()
    # author=scrapy.Field()
    # yuanWen=scrapy.Field()
    # shangXi=scrapy.Field()
    # pagelink=scrapy.Field()
class ShijingSCMJItem(scrapy.Item):
    title=scrapy.Field()
    author=scrapy.Field()
    yuanWen=scrapy.Field()
    shangXi=scrapy.Field()
    pagelink=scrapy.Field()
class GushiwenwangItem(scrapy.Item):
    # pass
    title=scrapy.Field()
    textContent=scrapy.Field()
    ref_url=scrapy.Field()
