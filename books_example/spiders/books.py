# -*- coding: utf-8 -*-
from urllib import parse

import scrapy

from ..items import BooksItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.xpath('./div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
            book_item = BooksItem()
            book_item['name'] = name
            book_item['price'] = price
            yield book_item
        next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            print('next url: ', next_url)
            yield scrapy.Request(next_url, callback=self.parse)