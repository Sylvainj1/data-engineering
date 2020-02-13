# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id= scrapy.Field()
    title=scrapy.Field()
    # stockage=scrapy.Field()
    currentPrice=scrapy.Field()
    previousPrice=scrapy.Field()
    save=scrapy.Field()
    img=scrapy.Field()
    type = scrapy.Field()
    site=scrapy.Field()

# class BMItem(scrapy.item):
#     # id= scrapy.Field()
#     title=scrapy.Field()
#     currentPrice=scrapy.Field()
#     previousPrice=scrapy.Field()
#     save=scrapy.Field()
#     # img=scrapy.Field()
#     type = scrapy.Field()
