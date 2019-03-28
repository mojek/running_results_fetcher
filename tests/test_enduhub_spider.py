from running_results_fetcher.enduhub_spider import EnduhubSpider
from running_results_fetcher.runner import Runner


def test_creating_base_url():
    runner = Runner('Michal Mojek', 1980)
    EnduhubSpider.create_url(runner)
    assert EnduhubSpider.start_urls[0] == 'https://enduhub.com/pl/search/?name=Michal Mojek&page=1'
