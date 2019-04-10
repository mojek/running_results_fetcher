#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `running_results_fetcher` package."""

from unittest.mock import patch


@patch('running_results_fetcher.running_results_fetcher.'
       'SpiderRunner.download_raw_pages')
def test_fetch_data(download_raw_pages_mock, rrf,
                    spider_config, raw_page_html):
    runner = spider_config.runner
    download_raw_pages_mock.return_value = [raw_page_html]
    rrf.set_spider_config(spider_config)
    rrf.fetch_data_for_runner()
    assert runner.race_results[0].race_name == 'V Bieg Niepodległości'


# def test_fetch_data_for_runner(rrf, spider_config):
#     rrf.set_spider_config(spider_config)
#     rrf.fetch_data_for_runner()
#     assert rrf.data_downloaded is True
