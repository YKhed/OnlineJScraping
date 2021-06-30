# -*- coding: utf-8 -*-
import scrapy


class Hespress1Spider(scrapy.Spider):
    name = 'hespress1'
    allowed_domains = ['www.hespress.com']
    start_urls = ['https://www.hespress.com/%d8%b9%d8%af%d8%af-%d8%a7%d9%84%d9%85%d9%84%d9%82%d8%ad%d9%8a%d9%86-%d8%a8%d8%a7%d9%84%d9%83%d8%a7%d9%85%d9%84-%d9%8a%d8%aa%d8%ac%d8%a7%d9%88%d8%b2-%d8%b9%d8%aa%d8%a8%d8%a9-9-%d9%85%d9%84%d8%a7%d9%8a-843790.html']

    def parse(self, response):
        comments = response.xpath("//ul[@class='comment-list hide-comments ']/li")
        for comment in comments :
            content = comment.xpath(".//div/div[@class='comment-text']/p/text()").get()
            yield {
                'content' : content
            }

