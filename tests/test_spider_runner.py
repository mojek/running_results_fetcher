from running_results_fetcher.spider_runner import SpiderRunner
from unittest.mock import patch


@patch('running_results_fetcher.spider_runner.CrawlerProcess.start')
def test_set_download_data_to_true(endu_spider, runner, spider_config):
    spider_runner = SpiderRunner(endu_spider, spider_config)
    spider_runner.download_raw_pages()
    assert spider_runner.finished is True
