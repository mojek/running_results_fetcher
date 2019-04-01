from running_results_fetcher.spider import Spider
from running_results_fetcher.runner import Runner
from running_results_fetcher.spider_config import SpiderConfig


def test_start_urlr_with_injected_configuration():
    runner = Runner('Michał Mojek', 1980)
    config = SpiderConfig(domain_name='enduhub.com')
    config.runner = runner
    config.url_suffix = "/pl/search/?name={}&page=1".format(runner.name)
    Spider.set_config(config)
    url_for_test = 'https://enduhub.com/pl/search/?name=Michał Mojek&page=1'
    assert Spider.start_urls[0] == url_for_test


def test_allowed_domain_with_injected_configuration():
    runner = Runner('Michał Mojek', 1980)
    config = SpiderConfig(domain_name='enduhub.com')
    config.runner = runner
    config.url_suffix = "/pl/search/?name={}&page=1".format(runner.name)
    Spider.set_config(config)
    assert Spider.allowed_domains[0] == 'enduhub.com'
