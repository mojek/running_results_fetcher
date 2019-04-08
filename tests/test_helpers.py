
from datetime import timedelta
from datetime import date
from running_results_fetcher.helpers import string_to_timedelta
from running_results_fetcher.helpers import string_to_date
from running_results_fetcher.helpers import convert_distance


def test_string_to_timedelta():
    timedelta_string = '00:00:12'
    assert isinstance(string_to_timedelta(timedelta_string), timedelta)
    assert string_to_timedelta(timedelta_string).seconds == 12


def test_string_to_date():
    strint_date = '2018-11-10'
    assert isinstance(string_to_date(strint_date), date)
    assert string_to_date(strint_date) == date(2018, 11, 10)


def test_convert_distance_return_type():
    assert isinstance(convert_distance(10), float)
    assert convert_distance(None) is None
    assert isinstance(convert_distance('10 km'), float)


def test_convert_distance_when_empty_string():
    assert convert_distance(' ') is None
    assert convert_distance('km') is None
    assert convert_distance('') is None


def test_convert_distance_in_km():
    assert convert_distance('10km') == 10.0
    assert convert_distance(' 20 km ') == 20.0


def test_convert_distance_maraton():
    assert convert_distance('maraton') == 42.1
    assert convert_distance('Maraton') == 42.1
    assert convert_distance('MaratoN') == 42.1
    assert convert_distance(' MaratoN ') == 42.1


def test_convert_distance_polmaraton():
    assert convert_distance('połmaraton') == 21.05
    assert convert_distance('polmaraton') == 21.05
    assert convert_distance('Polmaraton') == 21.05
    assert convert_distance(' Połmaraton ') == 21.05
