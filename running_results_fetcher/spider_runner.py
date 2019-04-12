from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor


class SpiderRunner:
    """It's responsible for running spiders"""

    def __init__(self, spider, spider_config):
        self.spider = spider
        self.spider.set_config(spider_config)

    def download_raw_pages(self):
        process = CrawlerRunner({
            'USER_AGENT':
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        crawler = process.crawl(self.spider)

        self.spider.raw_pages = []
        self.finished = True
        crawler.addBoth(lambda _: reactor.stop())
        reactor.run()
        raw_pages = self.spider.raw_pages
        return raw_pages

    def __str__(self):
        return "{} {}".format(self.spider.name,
                              self.spider.spider_config.start_url)
