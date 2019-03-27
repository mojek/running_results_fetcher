from pytest import fixture
from running_results_fetcher.runner import Runner
from running_results_fetcher.fetcher_manager import FetcherManager


@fixture(scope="function")
def runner():
    return Runner('Michal Mojek')


@fixture(scope="function")
def fetcher_manager():
    return FetcherManager()
