#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `running_results_fetcher` package."""

import pytest

from click.testing import CliRunner

from running_results_fetcher import running_results_fetcher
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


def test_fetch_data(runner, rrf):
    rrf.set_runner(runner)
    # rrf.fetch_data()
    #assert rrf.data_downloaded == True
