import scrapy


class EnduhubSpider(scrapy.Spider):
    allowed_domains = ["enduhub.com"]
    name = "enduhub"
    url_domain_name = "https://enduhub.com"
    start_urls = []

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
    def create_url(cls, runner):
        cls.start_urls.append(
            "{}/pl/search/?name={}&page=1"
            .format(cls.url_domain_name, runner.name))

    def __find_next_page(self, response):
        NEXT_PAGE_SELECTOR = '.pagination .pages .active + li a::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        return next_page
