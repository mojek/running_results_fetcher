#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `running_results_fetcher` package."""

from unittest.mock import patch
from running_results_fetcher.app import RunningResultFetcher

@patch('running_results_fetcher.app.'
       'SpiderRunner.download_raw_pages')
def test_fetch_data(download_raw_pages_mock, rrf,
                    spider_config, raw_page_html):
    runner = spider_config.runner
    download_raw_pages_mock.return_value = [raw_page_html]
    rrf.set_spider_config(spider_config)
    rrf.fetch_data_for_runner()
    assert runner.race_results[0].race_name == 'V Bieg Niepodległości'

@patch('running_results_fetcher.app.'
       'SpiderRunner.download_raw_pages')
def test_api(download_raw_pages_mock, raw_page_html):
    fetcher = RunningResultFetcher('Michał Mojek', 1980)
    download_raw_pages_mock.return_value = [raw_page_html]
    runner = fetcher.fetch_data_for_runner()
    assert runner.stats.km_count() == 564.25
    assert str(runner.stats.best_time_on_distance('10 km')) == "0:39:49"
    assert runner.stats.longest_run() == 64


# def test_fetch_data_for_runner(rrf, spider_config):
#     rrf.set_spider_config(spider_config)
#     rrf.fetch_data_for_runner()
#     assert rrf.data_downloaded is True
