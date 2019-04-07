
from datetime import timedelta
from datetime import date
from running_results_fetcher.helpers import string_to_timedelta, string_to_date


def test_string_to_timedelta():
    timedelta_string = '00:00:12'
    assert isinstance(string_to_timedelta(timedelta_string), timedelta)
    assert string_to_timedelta(timedelta_string).seconds == 12


def test_string_to_date():
    strint_date = '2018-11-10'
    assert isinstance(string_to_date(strint_date), date)
    assert string_to_date(strint_date) == date(2018, 11, 10)
