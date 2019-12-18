# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ArticleItem


class AppleSpider(scrapy.Spider):
    name = 'applescrap'
    allowed_domains = ['apple.com']
    start_urls = ['https://www.apple.com/fr/shop/refurbished/mac',
    'https://www.apple.com/fr/shop/refurbished/ipad',
    'https://www.apple.com/fr/shop/refurbished/iphone',
    'https://www.apple.com/fr/shop/refurbished/ipod',
    ]

    def clean_spaces(self,string):
                if string:
                    return " ".join(string.split())

    def parse(self, response):
        all_links = {
            name:response.urljoin(url) for name,url in zip(
            response.css(".refurbished-category-grid-no-js").css("li").css("a::text").extract(),
            response.css(".refurbished-category-grid-no-js").css("li").css("a::attr(href)").extract()
            )
        }
        for link in all_links.values():
            yield Request(link, callback=self.refurbished_product)
            print(link)

    def refurbished_product(self, response):
        for i in response.css(".platter.selfclear"):
            title=self.clean_spaces(i.css("#productDetails").css("h1::text").get())
            currentPrice=self.clean_spaces(i.css(".current_price span::text").get())
            previousPrice=self.clean_spaces(i.css(".as-price-previousprice::text").get())
            save=self.clean_spaces(i.css(".as-price-savings::text").get())
            img=i.css(".gallery-preview img::attr(src)").extract() 
            yield ArticleItem(
                    title=title,
                    currentPrice=currentPrice,
                    previousPrice=previousPrice,
                    save=save,
                    img=img
                )

    