from scrapy.crawler import CrawlerProcess


class SpiderRunner:
    """It's responsible for running spiders"""

    def __init__(self, spider, spider_config):
        self.spider = spider
        self.spider.set_config(spider_config)

    def download_raw_pages(self):
        process = CrawlerProcess({
            'USER_AGENT':
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(self.spider)
        process.start()
        raw_pages = self.spider.raw_pages
        self.spider.raw_pages = []
        self.finished = True
        return raw_pages

    def __str__(self):
        return "{} {}".format(self.spider.name,
                              self.spider.spider_config.start_url)
