import scrapy
from .spider_config import SpiderConfig


class Spider(scrapy.Spider):
    allowed_domains = []
    start_urls = []
    raw_pages = []
    protocol = 'https://'
    spider_config = SpiderConfig()
    next_page_selector = None

    def parse(self, response):
        self.raw_pages.append(response.body)
        next_page = self.__find_next_page(response)
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse)

    @classmethod
    def set_config(cls, config):
        cls.spider_config = config
        cls.protocol = config.protocol
        cls.domain_name = config.domain_name
        cls.name = config.name
        cls.start_urls.append(config.start_url)
        cls.allowed_domains.append(cls.domain_name)
        cls.next_page_selector = config.next_page_selector

    @classmethod
    def __find_next_page(cls, response):
        next_page = response.css(cls.next_page_selector).extract_first()
        return next_page
