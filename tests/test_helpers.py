
from datetime import timedelta
from running_results_fetcher.helpers import string_to_timedelta


def test_string_to_timedelta():
    assert isinstance(string_to_timedelta('00:39:12'), timedelta)
    assert string_to_timedelta('00:00:12').seconds == 12
