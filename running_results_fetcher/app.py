from .enduhube_page_parser import EnduhubPageParser
from .spider import Spider
from .spider_runner import SpiderRunner
from .spider_config import SpiderConfig
from .runner import Runner


class RunningResultFetcher:
    """This class manage all functionality of the package"""

    def __init__(self, runner_name, runner_birth_year, **kwargs):
        self.runner = Runner(runner_name, runner_birth_year)

        self.spider_config = kwargs.get(
            'spider_config', config_spider(self.runner))

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


def config_spider(runner):
    config = SpiderConfig(domain_name='enduhub.com')
    config.runner = runner
    config.url_suffix = "/pl/search/?name={}&page=1".format(
        runner.name)
    selctor = '.pagination .pages .active + li a::attr(href)'
    config.next_page_selector = selctor
    return config
