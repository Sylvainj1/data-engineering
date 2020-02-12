# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ArticleItem
import re 
#les pipelines on été commenté dans les settings pour le moment pour eviter de stocker les elements back market dans mongo et ES
#pour activer certaines pipelines en fonction de la spider https://stackoverflow.com/questions/8372703/how-can-i-use-different-pipelines-for-different-spiders-in-a-single-scrapy-proje

class BackMarketSpider(scrapy.Spider):
    name = 'backmarketscrap'
    allowed_domains = ['www.backmarket.fr']
    start_urls = ['https://www.backmarket.fr/smartphones-reconditionnes.html',
    'https://www.backmarket.fr/macbook-reconditionne.html',
    'https://www.backmarket.fr/ipad/pro-reconditionnes.html'
    ]
    custom_settings = {
        'FEED_URI' : 'back_market.json'  #scrapy crawl applescrap pour lancer le scrapping
    }


    def clean_spaces(self,string):
                if string:
                    return " ".join(string.split())

    def parse(self, response):
        # product_div = response.css('._1qrr_qTIsEL2tmG4ryaDXb').css('._3tkNFs_kHyB1po1mbEBzMN').css('._2dwmPkboUBu5DEG9DooXmT').css('._3m6PyEa1cAm3e8H-zlG4w1').css('.productDescription')
        # for i in product_div:
        #     #voir pour un id
        #     title = self.clean_spaces(i.css('h2::text').get())
        #     stockage=re.sub("[^\d\.]", "", self.clean_spaces(i.css('h2::text').extract()[1:-1]))
        #     currentPrice = self.clean_spaces(i.css('.price::text').get())
        #     previousPrice = self.clean_spaces(i.css('.price.primary.small::text').get())
        #     save = 'unknown'
        #     img = i.css('.nullclass').get() #pour créer une valeur null sur la clé image pour le moment comme les images sont pas chopés
        #     type = self.clean_spaces(title.split()[0])
        
        for i in response.css('._1qrr_qTIsEL2tmG4ryaDXb').css('._3tkNFs_kHyB1po1mbEBzMN').css('._2dwmPkboUBu5DEG9DooXmT').css('a'):
            title=self.clean_spaces(i.css('h2::text').get())
            stockage=re.findall("\d+",title)
            stockage = [int(e) for e in stockage]
            for e in stockage:
                if e>2000 :
                    stockage.remove(e)
            stockage=max(stockage)       
            currentPrice=self.clean_spaces(i.css('.price::text').get())
            previousPrice=self.clean_spaces(i.css('.price.primary.small::text').get())
            save=''
            img=i.css('.nullclass').get()
            type=self.clean_spaces(title.split()[0])

            yield ArticleItem(
                id="",
                title=title,
                stockage=stockage,
                currentPrice=currentPrice,
                previousPrice=previousPrice,
                save=save,
                img = img,
                type = type,
                site='backmarket'
            )
            


