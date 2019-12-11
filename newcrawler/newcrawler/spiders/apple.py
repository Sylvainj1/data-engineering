# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ArticleItem


class AppleSpider(scrapy.Spider):
    name = 'apple'
    allowed_domains = ['apple.com']
    start_urls = ['https://www.apple.com/fr/shop/refurbished/mac',
    'https://www.apple.com/fr/shop/refurbished/ipad',
    'https://www.apple.com/fr/shop/refurbished/iphone',
    'https://www.apple.com/fr/shop/refurbished/accessories',
    'https://www.apple.com/fr/shop/refurbished/ipod',
    'https://www.apple.com/fr/shop/refurbished/appletv',
    'https://www.apple.com/fr/shop/refurbished/clearance',
    ]

    def parse(self, response):
        for i in response.css(".refurbished-category-grid-no-js").css("li"):
            title=i.css("h3").css("a::text").extract()
            currentPrice=i.css(".as-price-currentprice::text").extract()
            previousPrice=i.css(".as-price-previousprice::text").extract()   
            save=i.css(".as-producttile-savingsprice::text").extract() 
            yield ArticleItem(
                    title=title,
                    currentPrice=currentPrice,
                    previousPrice=previousPrice,
                    save=save,
                )

        # all_links = response.urljoin(response.css(".ac-gf-directory-column-section-link")[23].css("a::attr(href)").extract()[0])
       
        # all_links = {
        #     response.urljoin(url) for url in zip(
        #         response.urljoin(response.css(".ac-gf-directory-column-section-link")[23].css("a::attr(href)").extract()[0])
        #     )
        # }
        
        # for link in all_links:
        # yield Request(all_links, callback=self.refurbished_product)
        # yield{
        #     "link":all_links
        # }


    def refurbished_product(self, response):
        for i in response.css("li"):
            title=i.response.css("h4").css("a::text").extract()    
            currentPrice=i.response.css(".as-price-currentprice::text").extract()
            previousPrice=i.response.css(".as-price-previousprice::text").extract()   
            save=response.i.css(".as-producttile-savingsprice::text").extract() 
            yield ArticleItem(
                    title=title,
                    currentPrice=currentPrice,
                    previousPrice=previousPrice,
                    save=save,
                )
