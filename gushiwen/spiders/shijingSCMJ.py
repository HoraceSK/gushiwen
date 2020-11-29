# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gushiwen.items import ShijingSCMJItem

class ShijingscmjSpider(CrawlSpider):
    name = 'shijingSCMJ'
    allowed_domains = ['www.shicimingju.com']
    start_urls = ['http://www.shicimingju.com/chaxun/zuozhe/13046.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+chaxun/zuozhe/13046(_*\d*)?\.html'),follow=True),
        Rule(LinkExtractor(allow=r'.+chaxun/list/\d+\.html'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        title=response.xpath(r'//h1/text()').get().strip()
        author=response.xpath(r'//div[@class="niandai_zuozhe"]//a/text()').get().strip()
        yuanWen=''.join(response.css(r'#zs_content::text').getall()).strip()
        shangXi=''.join(response.css(r'div.shangxi_content::text').getall()).strip()
        pagelink=response.url
        # print(yuanWen)
        item=ShijingSCMJItem(
            title=title,
            author=author,
            yuanWen=yuanWen,
            shangXi=shangXi,
            pagelink=pagelink
        )
        return item
