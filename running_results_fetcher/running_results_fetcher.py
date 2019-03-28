# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from running_results_fetcher.enduhub_spider import EnduhubSpider


class RunningResultFetcher:
    """This class manage all functionality of the package"""

    def __init__(self):
        self.data_downloaded = False

    def set_runner(self, runner):
        """Add runner to Fetcher Manager"""
        self.runner = runner

    def fetch_data(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        EnduhubSpider.create_url(self.runner)
        process.crawl(EnduhubSpider)
        process.start()
        self.data_downloaded = True
