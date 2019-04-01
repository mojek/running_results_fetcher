from running_results_fetcher.spider_config import SpiderConfig
from running_results_fetcher.runner import Runner


def test_set_name_from_domain():
    config = SpiderConfig()
    config.domain_name = 'enduhub.com'
    assert config.name == 'enduhub'


def test_default_protocol():
    config = SpiderConfig()
    assert config.protocol == 'https://'


def test_stater_url():
    config = SpiderConfig(domain_name='enduhub.com')
    runner = Runner('Michał Mojek', 1980)
    config.url_suffix = "/pl/search/?name={}&page=1".format(runner.name)
    url_for_test = 'https://enduhub.com/pl/search/?name=Michał Mojek&page=1'
    assert config.start_url == url_for_test
