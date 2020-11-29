# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gushiwen.items import GushiwenwangItem

class GushiwenwangSpider(CrawlSpider):
    name = 'gushiwenwang'
    allowed_domains = ['www.gushiwen.cn']
    # start_urls = ['https://www.gushiwen.org/guwen/sunzi.aspx']
    start_urls = [
    'https://so.gushiwen.cn/guwen/bookv_39.aspx',
    'https://so.gushiwen.cn/guwen/bookv_40.aspx',
    'https://so.gushiwen.cn/guwen/bookv_41.aspx',
    'https://so.gushiwen.cn/guwen/bookv_42.aspx',
    'https://so.gushiwen.cn/guwen/bookv_43.aspx',
    'https://so.gushiwen.cn/guwen/bookv_44.aspx',
    'https://so.gushiwen.cn/guwen/bookv_45.aspx',
    'https://so.gushiwen.cn/guwen/bookv_46.aspx',
    'https://so.gushiwen.cn/guwen/bookv_47.aspx',
    'https://so.gushiwen.cn/guwen/bookv_48.aspx',
    'https://so.gushiwen.cn/guwen/bookv_49.aspx',
    'https://so.gushiwen.cn/guwen/bookv_50.aspx',
    'https://so.gushiwen.cn/guwen/bookv_51.aspx'
     ]
    rules = (
        Rule(LinkExtractor(allow=r'.+guwen/.+(book|sunzi)?\d*\.aspx'),follow=True),
        Rule(LinkExtractor(allow=r'.+guwen/bookv_*\d*\.aspx'), callback='parse_item', follow=False)
    )
    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # if response.status==302:
            # yield scrapy.Request(response.url,callback=self.parse_item,dont_filter=True)
        # else:
            # pass
        title=response.css(r'div.cont>h1>span>b::text').get()
        textContent=r''.join(response.css(r'div.contson>p::text').getall()).strip()
        ref_url=response.url
        item=GushiwenwangItem(
            title=title,
            textContent=textContent,
            ref_url=ref_url
        )
        print('#'*30)
        print(ref_url)
        return item
