#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `running_results_fetcher` package."""

from unittest.mock import patch
from click.testing import CliRunner


from running_results_fetcher import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'running_results_fetcher.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


@patch('running_results_fetcher.running_results_fetcher.'
       'SpiderRunner.download_raw_pages')
def test_fetch_data_and_download_data_to_true(SpiderRunnerMock, rrf,
                                              spider_config, raw_page_html):
    rrf.set_spider_config(spider_config)
    # TODO monkey patching do right test
    rrf.fetch_data_for_runner()
    assert rrf.data_downloaded is True


# def test_fetch_data_for_runner(rrf, spider_config):
#     rrf.set_spider_config(spider_config)
#     rrf.fetch_data_for_runner()
#     assert rrf.data_downloaded is True
