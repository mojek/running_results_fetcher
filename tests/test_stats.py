from running_results_fetcher.stats import Stats
from datetime import date


def test_init(runner):
    stats = Stats(runner)
    assert stats.runner is runner
    assert stats.race_type is None
    assert stats.from_date is None
    assert stats.to_date is None


def test_parsing_froom_date(runner):
    stats = Stats(runner, from_date="2018-11-10")
    assert stats.from_date == date(2018, 11, 10)


def test_parsing_to_date(runner):
    stats = Stats(runner, to_date="2018-11-10")
    assert stats.to_date == date(2018, 11, 10)
