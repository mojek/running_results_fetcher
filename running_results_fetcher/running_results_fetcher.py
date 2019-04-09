from .spider_runner import SpiderRunner
from .spider import Spider
from .enduhube_page_parser import EnduhubPageParser
# from .enduhube_page_parser import EnduhubPageParser


class RunningResultFetcher:
    """This class manage all functionality of the package"""

    def __init__(self, **kwargs):
        self.spider_config = kwargs.get('spider_config')

    def set_spider_config(self, spider_config):
        self.spider_config = spider_config

    def fetch_data_for_runner(self):
        spider = SpiderRunner(Spider, self.spider_config)
        runner = self.spider_config.runner
        raw_pages = spider.download_raw_pages()
        for raw_page in raw_pages:
            page = EnduhubPageParser(raw_page)
            races = page.parse_page()
            runner.add_races(races)
        return runner
