# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gushiwen.items import ShiciByAuthorItem
# from gushiwen.items import ShiciByMarkItem

class ShicimingjuSpider(CrawlSpider):
    name = 'shicimingju'
    allowed_domains = ['www.shicimingju.com']
    # start_urls = ['http://www.shicimingju.com']
    start_urls = ['http://www.shicimingju.com/shicimark/miaoxiexiatiantian.html']
    rules = (
        # Rule(LinkExtractor(allow=r'.+'),follow=True),
        # Rule(LinkExtractor(allow=r'.+chaxun/zuozhe/\d*(_\d*)?\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'.+shicimark/.+\.html'),follow=True),
        # Rule(LinkExtractor(allow=r'.+shicimark/.+\.html'), callback='parse_mark', follow=False),
        Rule(LinkExtractor(allow=r'.+chaxun/list/\d*(_*\d*)?\.html'), callback='parse_author', follow=False)
    )
    def parse_author(self, response):
        title=response.xpath(r'//h1/text()').get().strip()
        author=response.xpath(r'//div[@class="niandai_zuozhe"]/text()').get().strip()+response.xpath(r'//div[@class="niandai_zuozhe"]//a/text()').get().strip()
        yuanWen=''.join(response.css(r'#zs_content::text').getall()).strip()
        shangXi=''.join(response.css(r'div.shangxi_content::text').getall()).strip()
        pagelink=response.url
        item=ShiciByAuthorItem(
            title=title,
            author=author,
            yuanWen=yuanWen,
            shangXi=shangXi,
            pagelink=pagelink
        )
        print(
            title,
            author,
            yuanWen,
            shangXi,
            pagelink
        )
        return item
    # def parse_mark(self, response):
        # title=response.xpath(r'//h1/text()').get().strip()
        # author=response.xpath(r'//div[@class="niandai_zuozhe"]//a/text()').get().strip()
        # yuanWen=''.join(response.css(r'#zs_content::text').getall()).strip()
        # shangXi=''.join(response.css(r'div.shangxi_content::text').getall()).strip()
        # pagelink=response.url
        # item=ShiciByMarkItem(
            # title=title,
            # author=author,
            # yuanWen=yuanWen,
            # shangXi=shangXi,
            # pagelink=pagelink
        # )
        # return item
