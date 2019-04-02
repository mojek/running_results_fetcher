from .spider_runner import SpiderRunner
from .spider import Spider
# from .enduhube_page_parser import EnduhubPageParser


class RunningResultFetcher:
    """This class manage all functionality of the package"""

    def __init__(self, **kwargs):
        self.data_downloaded = False
        self.spider_config = kwargs.get('spider_config')

    def set_spider_config(self, spider_config):
        self.spider_config = spider_config

    def fetch_data_for_runner(self):
        spider = SpiderRunner(Spider, self.spider_config)
        raw_pages = spider.download_raw_pages()
        # TODO extrackt results and add to runner
        for raw_page in raw_pages:
            pass
            # page = EnduhubPageParser(raw_page)
            # list_of_races = page.parse_page()

        self.data_downloaded = True
