# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
from gushiwen.items import ShijingScanItem
from gushiwen.items import ShijingSingleItem
from gushiwen.items import YemengdeItem
from gushiwen.items import ShiciByAuthorItem
# from gushiwen.items import ShiciByMarkItem
from gushiwen.items import ShijingSCMJItem
from gushiwen.items import GushiwenwangItem


class GushiwenPipeline(object):
    def process_item(self, item, spider):
        return item
class ShijingScanPipeline(object):
    def __init__(self):
        self.fp=open("scan诗经.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print(r'在下不过是一介貂蝉，还望阁下不吝赐教！')
    def close_spider(self,spider):
        self.fp.close()
        print(r'你若觉得有实力跟我玩，小蝉不介意奉陪到底。')
    def process_item(self, item, spider):
        if isinstance(item,ShijingScanItem):
            self.exporter.export_item(item)
        return item
class ShijingSinglePipeline(object):
    def __init__(self):
        self.fp=open("single诗经.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print(r'在下不过是一介貂蝉，还望阁下不吝赐教！')
    def close_spider(self,spider):
        self.fp.close()
        print(r'你若觉得有实力跟我玩，小蝉不介意奉陪到底。')
    def process_item(self, item, spider):
        if isinstance(item,ShijingSingleItem):
            self.exporter.export_item(item)
        return item
class YemengdePipeline(object):
    def __init__(self):
        self.fp=open("yemd106-叶梦得.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print(r'在下不过是一介貂蝉，还望阁下不吝赐教！')
    def close_spider(self,spider):
        self.fp.close()
        print(r'你若觉得有实力跟我玩，小蝉不介意奉陪到底。')
    def process_item(self, item, spider):
        if isinstance(item,YemengdeItem):
            self.exporter.export_item(item)
        return item
class ShiciByAuthorPipeline(object):
    def __init__(self):
        self.fp=open("shiciByAuthor.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print(r'在下不过是一介貂蝉，还望阁下不吝赐教！')
    def close_spider(self,spider):
        self.fp.close()
        print(r'你若觉得有实力跟我玩，小蝉不介意奉陪到底。')
    def process_item(self, item, spider):
        if isinstance(item,ShiciByAuthorItem):
            self.exporter.export_item(item)
        return item
# class ShiciByMarkPipeline(object):
    # def __init__(self):
        # self.fp=open("shiciByMark.json",'wb')
        # self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    # def open_spider(self,spider):
        # print(r'在下不过是一介貂蝉，还望阁下不吝赐教！')
    # def close_spider(self,spider):
        # self.fp.close()
        # print(r'你若觉得有实力跟我玩，小蝉不介意奉陪到底。')
    # def process_item(self, item, spider):
        # if isinstance(item,ShiciByMarkItem):
            # self.exporter.export_item(item)
        # return item

class ShijingSCMJPipeline(object):
    def __init__(self):
        self.fp=open("shijing-诗经-诗词名句网.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print(r'在下不过是一介貂蝉，还望阁下不吝赐教！')
    def close_spider(self,spider):
        self.fp.close()
        print(r'你若觉得有实力跟我玩，小蝉不介意奉陪到底。')
    def process_item(self, item, spider):
        if isinstance(item,ShijingSCMJItem):
            self.exporter.export_item(item)
        return item
class GushiwenwangPipeline(object):
    def __init__(self):
        self.fp=open("export古诗文网.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print(r'在下不过是一介貂蝉，还望阁下不吝赐教！')
    def close_spider(self,spider):
        self.fp.close()
        print(r'你若觉得有实力跟我玩，小蝉不介意奉陪到底。')
    def process_item(self, item, spider):
        print(item['title'])
        print(item['textContent'])
        print(item['ref_url'])
        if isinstance(item,GushiwenwangItem):
            self.exporter.export_item(item)
            return item
