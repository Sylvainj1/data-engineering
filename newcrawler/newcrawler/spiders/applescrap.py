# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ArticleItem
import re

class AppleSpider(scrapy.Spider):
    name = 'applescrap'
    allowed_domains = ['apple.com']
    start_urls = ['https://www.apple.com/fr/shop/refurbished/mac',
    'https://www.apple.com/fr/shop/refurbished/ipad',
    'https://www.apple.com/fr/shop/refurbished/iphone',
    'https://www.apple.com/fr/shop/refurbished/ipod',
    ]
    # custom_settings = {
    #     'FEED_URI' : 'apple.json'  #scrapy crawl applescrap pour lancer le scrapping
    # }


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
            id = i.css('form').css('input::attr(value)')[0].get()  #ca n'a pas l'air d'etre unique bizarre
            title = self.clean_spaces(i.css("#productDetails").css("h1::text").get())
            # stockage= re.sub("[^\d\.]", "", self.clean_spaces(i.css("#dimensionCapacity.product-variation-list.form-dropdown.form-textbox").css("option[selected='selected']::text").extract_first()))
            # stockage=int(stockage)
            currentPrice = self.clean_spaces(i.css(".current_price span::text").get())
            previousPrice = i.css(".as-price-previousprice::text").get()
            save = i.css(".as-price-savings::text").get()
            img= i.css(".gallery-preview img::attr(src)").extract()
            type = title.split()[0]
            yield ArticleItem(
                    id= id,
                    title=title,
                    # stockage=stockage,
                    currentPrice=currentPrice,
                    previousPrice=previousPrice,
                    save=save,
                    img=img,
                    type = type,
                    site='apple',
                )
