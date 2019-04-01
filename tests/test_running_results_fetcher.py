#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `running_results_fetcher` package."""

from unittest.mock import patch
from click.testing import CliRunner

from running_results_fetcher.runner import Runner
from running_results_fetcher import cli


def test_set_runner_to_running_results_fetcher(runner, rrf):
    rrf.set_runner(runner)
    assert isinstance(rrf.runner, Runner)


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'running_results_fetcher.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


@patch('running_results_fetcher.running_results_fetcher.SpiderRunner.start')
def test_fetch_data_and_set_download_data_to_true(SpiderRunnerMock, rrf, runner):
    rrf.set_runner(runner)
    rrf.fetch_data()
    assert rrf.data_downloaded is True


# def test_fetch_data(runner, rrf):
#     rrf.set_runner(runner)
#     print('tests')
#     rrf.fetch_data()
#     assert rrf.data_downloaded is True
