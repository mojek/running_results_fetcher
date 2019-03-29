# -*- coding: utf-8 -*-
from running_results_fetcher.spider_runner import SpiderRunner
from running_results_fetcher.enduhub_spider import EnduhubSpider


class RunningResultFetcher:
    """This class manage all functionality of the package"""

    def __init__(self):
        self.data_downloaded = False

    def set_runner(self, runner):
        """set runner to fetcher"""
        self.runner = runner

    def fetch_data(self):
        spider = SpiderRunner(EnduhubSpider, self.runner)
        spider.start()
        self.data_downloaded = True
