# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


class MongodbPipeline(object):
    collection_name = "comments"
    
    def open_spider(self, spider) : 
        self.client = pymongo.MongoClient("mongodb+srv://scrapyYK:Jabouralol1.@cluster0.ac6mx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client("HESPRESS")

    def close_spider(self, spider) :
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection.name].insert(item)
        return item
