import scrapy
from running_results_fetcher.spider_config import SpiderConfig


class EnduhubSpider(scrapy.Spider):
    allowed_domains = []
    start_urls = []
    pages = []
    protocol = 'https://'
    config = SpiderConfig()

    def parse(self, response):
        page = response.url[-1]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        next_page = self.__find_next_page(response)
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse)

    @classmethod
    def set_config(cls, config):
        cls.protocol = config.protocol
        cls.domain_name = config.domain_name
        cls.name = config.name
        cls.start_urls.append(config.start_url)
        cls.allowed_domains.append(cls.domain_name)

    @classmethod
    def __find_next_page(self, response):
        NEXT_PAGE_SELECTOR = '.pagination .pages .active + li a::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        return next_page

    @classmethod
    def add_page(cls, page):
        cls.pages.append(page)
