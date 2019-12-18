# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from pymongo import MongoClient
import hashlib
import time

class TextPipeline(object):

    def process_item(self, item, spider):
        if item:
            item["_id"] = hashId(clean_spaces(item["_id"]))
            item["title"] = clean_spaces(item["title"])
            item['currentPrice'] = clean_spaces(item['currentPrice'])
            item['previousPrice'] = clean_spaces(item['previousPrice'])
            item['save'] = clean_spaces(item['save'])
            return item
        else:
            raise DropItem("Missing value in %s" % item)


def clean_spaces(string):
    if string:
        return " ".join(string.split())

def hashId(string):
    hashcode = str(int(time.time())).encode('utf-8')
    _id = hashlib.sha1(hashcode).hexdigest()[:11] + string
    return _id



class StoreInMongo(object):

    collection_name = 'product'

    def open_spider(self, spider):
        self.client = MongoClient("0.0.0.0:27018") #verif ca fonctionne sur un autre pc ????
        self.db = self.client.refurbApple

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item