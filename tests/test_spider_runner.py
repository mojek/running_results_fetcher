from running_results_fetcher.spider_runner import SpiderRunner
from unittest.mock import patch


@patch('running_results_fetcher.spider_runner.CrawlerProcess.start')
def test_fetch_data_and_set_download_data_to_true(endu_spider, runner):
    spider_runner = SpiderRunner(endu_spider, runner)
    spider_runner.start()
    assert spider_runner.finished is True
