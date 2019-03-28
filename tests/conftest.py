from pytest import fixture
from running_results_fetcher.runner import Runner
from running_results_fetcher.running_results_fetcher import RunningResultFetcher


@fixture(scope="function")
def runner():
    return Runner('Michal Mojek', 1980)


@fixture(scope="function")
def rrf():
    return RunningResultFetcher()
