# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class MongodbPipeline(object):
    collection_name = "article_comments"
    def open_spider(self, spider) :
        self.client = MongoClient("mongodb+srv://yass:test@cluster0.ntuni.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["HESPRESS"]
    
    def close_spider(self, spider) :
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
        
        
