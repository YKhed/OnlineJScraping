# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

class Hespress1Spider1(scrapy.Spider):
    name = 'hespress1'
    allowed_domains = ['www.hespress.com']
    start_urls = ['https://www.hespress.com/%d8%b9%d8%af%d8%af-%d8%a7%d9%84%d9%85%d9%84%d9%82%d8%ad%d9%8a%d9%86-%d8%a8%d8%a7%d9%84%d9%83%d8%a7%d9%85%d9%84-%d9%8a%d8%aa%d8%ac%d8%a7%d9%88%d8%b2-%d8%b9%d8%aa%d8%a8%d8%a9-9-%d9%85%d9%84%d8%a7%d9%8a-843790.html']

    def parse(self, response):
        comments = response.xpath("//ul[@class='comment-list hide-comments ']/li")
        for comment in comments :
            content = comment.xpath(".//div/div[@class='comment-text']/p/text()").get()
            ratio = comment.xpath(".//div/div[@class='comment-footer row']/div/span[@class='comment-recat-number']/text()").get()
            date = comment.xpath(".//div/div[@class='comment-head']/div[@class='comment-date']/text()").get()
            yield {
                'content' : content,
                'ratio' : ratio,
                'date' : date
            }


class Hespress1Spider2(scrapy.Spider):
    name = 'hespress2'
    allowed_domains = ['www.hespress.com']
    start_urls = ['https://www.hespress.com/%d9%87%d8%a7%d9%84%d8%a7%d9%86%d8%af-%d9%8a%d9%87%d8%af%d8%af-%d8%a8%d9%82%d8%a7%d8%a1-%d8%b2%d9%8a%d8%a7%d8%b4-%d9%81%d9%8a-%d8%aa%d8%b4%d9%8a%d9%84%d8%b3%d9%8a-%d8%a7%d9%84%d8%a5%d9%86%d8%ac-848222.html']
    def parse(self, response):
        comments = response.xpath("//ul[@class='comment-list hide-comments ']/li")
        for comment in comments :
            content = comment.xpath(".//div/div[@class='comment-text']/p/text()").get()
            ratio = comment.xpath(".//div/div[@class='comment-footer row']/div/span[@class='comment-recat-number']/text()").get()
            date = comment.xpath(".//div/div[@class='comment-head']/div[@class='comment-date']/text()").get()
            yield {
                'content' : content,
                'ratio' : ratio,
                'date' : date
            }



process = CrawlerProcess()
process.crawl(Hespress1Spider1)
process.crawl(Hespress1Spider2)
process.start()
