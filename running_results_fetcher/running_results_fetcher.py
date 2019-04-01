from .spider_runner import SpiderRunner
from .spider import Spider
from .enduhube_page_parser import EnduhubPageParser


class RunningResultFetcher:
    """This class manage all functionality of the package"""

    def __init__(self, **kwargs):
        self.data_downloaded = False
        self.spider_config = kwargs.get('spider_config')

    def set_spider_config(self, spider_config):
        self.spider_config = spider_config

    def fetch_data(self):
        spider = SpiderRunner(Spider, self.spider_config)
        spider.start()
        for raw_page in self.spider_config.runner.raw_pages:
            page = EnduhubPageParser(raw_page)
            page.parse_page()
            self.data_downloaded = True
