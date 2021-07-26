# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

        
class SQLlitePipeline(object):
    def open_spider(self, spider) :
        self.connection = sqlite3.connect("hespress.db")
        self.c = self.connection.cursor()
        self.c.execute('''
            CREATE TABLE comments(
                content TEXT,
                ratio TEXT,
                date TEXT
            )        
        
        '''
        )
        self.connection.commit()

    def close_spider(self, spider) :
        self.client.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO comments (content,ratio,date) VALUES(?,?,?)

        ''', (
            item.get('content'),
            item.get('ratio'),
            item.get('date'),
        ))
        self.connection.commit()
        return item
        
        