# -*- coding: utf-8 -*-

"""Top-level package for Running Results Fetcher."""

__author__ = """Michal Mojek"""
__email__ = 'm.mojek@gmail.com'
__version__ = '0.1.0'

from running_results_fetcher.runner import Runner
from running_results_fetcher.spider_config import SpiderConfig
from running_results_fetcher.fetcher import Fetcher

__all__ = ['Runner', 'SpiderConfig', 'Fetcher']
