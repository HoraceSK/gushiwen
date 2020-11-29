# -*- coding: utf-8 -*-
import scrapy
import re
from gushiwen.items import ShijingScanItem
from gushiwen.items import ShijingSingleItem
baseUrl=r'http://www.wenyanhanyu.com'

class ShijingSpider(scrapy.Spider):
    name = 'shijing'
    allowed_domains = ['wenyanhanyu.com']
    start_urls = ['http://www.wenyanhanyu.com/shijing/']

    def parse(self, response):
        pass # 可惜不能区分篇章名字
        nameli=response.xpath(r'//div[@class="pleft"]//dd//a/text()').getall()
        linkli_fake=response.xpath(r'//div[@class="pleft"]//dd//a/@href').getall()
        linkli=[]
        for i in linkli_fake:
            tr_url=baseUrl+i
            linkli.append(tr_url)
        # print(nameli)
        # print(linkli)
        chapterRef=response.xpath(r'//div[@class="pleft"]').re(r'[\u4e00-\u9fa5]*·[\u4e00-\u9fa5]*|《[\u4e00-\u9fa5]*》')
        # chapterRef=[]
        # for i in chapterRef_fake:
            # a1=re.sub(r'\s*',r'',i)
            # chapterRef.append(a1)
        item=ShijingScanItem(
            chapterRef=chapterRef,
            nameli=nameli,
            linkli=linkli
        )
        yield item
        for i in linkli:
            yield scrapy.Request(i,callback=self.parse_page)
    def parse_page(self,response):
        title=response.xpath(r'//div[@class="title"]//h2/a/text()').get()
        pageLink=response.url
        yuanWen_fake="".join(response.xpath(r'//p[@align="center"]/text()').getall())
        yuanWen=re.sub(r'\s*','',yuanWen_fake)
        if len(yuanWen)==0:
            yuanWen=''.join(response.xpath(r'//div[@class="tagcoloer"]/p/text()').getall()).strip()
        zhuYiShang_fake=response.xpath(r'//h3/following-sibling::p/text()').getall()
        zhuYiShang=[]
        for i in zhuYiShang:
            a1=re.sub(r'\s*',r'',i)
            zhuYiShang.append(a1)
        item=ShijingSingleItem(
            title=title,
            pageLink=pageLink,
            yuanWen=yuanWen,
            zhuYiShang=zhuYiShang
        )
        yield item
