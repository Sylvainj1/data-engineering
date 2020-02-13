from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from newcrawler.newcrawler.spiders import applescrap
import os


class Scraper:
    def __init__(self):
        settings_file_path = 'newcrawler.newcrawler.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.settings = get_project_settings()
        self.process = CrawlerProcess(self.settings)
        self.spider = applescrap.AppleSpider 

    def run_spider(self):
        self.process.crawl(self.spider)
        self.process.start()  # le script se bloque ici jusqu'a la fin