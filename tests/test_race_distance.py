from running_results_fetcher.race_result import RaceResult


def test_race_results_distance_string_with_space():
    race_result = RaceResult(distance="10 km")
    assert race_result.distance == 10


def test_race_results_distance_string_without_space():
    race_result = RaceResult(distance="10km")
    assert race_result.distance == 10


def test_race_results_distance_have_float_type():
    race_result = RaceResult(distance=10)
    assert race_result.distance == 10.0
    assert isinstance(race_result.distance, float)


def test_race_results_distance_strig_maraton():
    race_result = RaceResult(distance='Maraton')
    assert race_result.distance == 42.1
    race_result = RaceResult(distance='maraton')
    assert race_result.distance == 42.1
    race_result = RaceResult(distance='mAraton')
    assert race_result.distance == 42.1


def test_race_results_distance_strig_polmaraton():
    race_result = RaceResult(distance='półmaraton')
    assert race_result.distance == 21.05
    race_result = RaceResult(distance='Półmaraton')
    assert race_result.distance == 21.05
    race_result = RaceResult(distance='półmaraton')
    assert race_result.distance == 21.05
