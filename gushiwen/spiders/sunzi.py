# -*- coding: utf-8 -*-
import scrapy
from gushiwen.items import GushiwenwangItem

from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("headless")
d1=webdriver.Chrome(options=option)
d1.get('https://www.gushiwen.cn/guwen/sunzi.aspx')
pgl_fake=d1.find_elements_by_css_selector(r'div.bookcont>ul>span>a')
pgl=[]
for i in pgl_fake:
    pgl.append(i.get_attribute('href'))
d1.quit()

class SunziSpider(scrapy.Spider):
    name = 'sunzi'
    allowed_domains = ['www.gushiwen.cn','www.gushiwen.org']
    # start_urls = [s
    # 'https://www.gushiwen.org/guwen/sunzi.aspx',
    # 'https://www.gushiwen.cn/guwen/sunzi.aspx'
    # ]
    # start_urls = [
    # 'https://so.gushiwen.cn/guwen/bookv_39.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_40.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_41.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_42.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_43.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_44.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_45.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_46.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_47.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_48.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_49.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_50.aspx',
    # 'https://so.gushiwen.cn/guwen/bookv_51.aspx'
     # ]
    start_urls = pgl
    def parse(self, response):
        pass
        title=response.css(r'div.cont>h1>span>b::text').get()
        textContent=r''.join(response.css(r'div.contson>p::text').getall()).strip()
        ref_url=response.url
        item=GushiwenwangItem(
            title=title,
            textContent=textContent,
            ref_url=ref_url
        )
        yield item
        # for i in pgl:
            # print(i)
            # yield scrapy.Request(i,callback=self.parse_page)
    # def parse_page(self, response):
        # pass
        # title=response.css(r'div.cont>h1>span>b::text').get()
        # textContent=r''.join(response.css(r'div.contson>p::text').getall()).strip()
        # ref_url=response.url
        # item=GushiwenwangItem(
            # title=title,
            # textContent=textContent,
            # ref_url=ref_url
        # )
        # yield item
