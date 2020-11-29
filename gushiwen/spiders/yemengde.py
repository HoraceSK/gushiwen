# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gushiwen.items import YemengdeItem

class YemengdeSpider(CrawlSpider):
    name = 'yemengde'
    allowed_domains = ['shicimingju.com']
    start_urls = ['http://www.shicimingju.com/chaxun/zuozhe/511.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+chaxun/zuozhe/511(_\d*)?\.html'),follow=True),
        Rule(LinkExtractor(allow=r'.+chaxun/list/\d+\.html'), callback='parse_yemengde', follow=False)
    )
    def parse_yemengde(self, response):
        #item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        title=response.xpath(r'//h1/text()').get().strip()
        author=response.xpath(r'//div[@class="niandai_zuozhe"]//a/text()').get().strip()
        yuanWen=''.join(response.css(r'#zs_content::text').getall()).strip()
        shangXi=''.join(response.css(r'div.shangxi_content::text').getall()).strip()
        pagelink=response.url
        # print(yuanWen)
        item=YemengdeItem(
            title=title,
            author=author,
            yuanWen=yuanWen,
            shangXi=shangXi,
            pagelink=pagelink
        )
        return item
