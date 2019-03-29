from scrapy.crawler import CrawlerProcess


class SpiderRunner:
    """It's responsible for running spiders"""

    def __init__(self, spider, runner):
        self.spider = spider
        self.runner = runner

    def start(self):
        process = CrawlerProcess({
            'USER_AGENT':
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        self.spider.create_url(self.runner)
        process.crawl(self.spider)
        process.start()
