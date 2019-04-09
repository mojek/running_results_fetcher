import datetime
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


def test_runner_brith_with_string():
    race_result = RaceResult(runner_birth='1980')
    assert race_result.runner_birth == 1980


def test_runner_brith_with_int():
    race_result = RaceResult(runner_birth=1980)
    assert race_result.runner_birth == 1980


def test_runner_brith_with_short_string():
    race_result = RaceResult(runner_birth='80')
    assert race_result.runner_birth == 1980


def test_runner_brith_with_its_not_numerical():
    race_result = RaceResult(runner_birth='-')
    assert race_result.runner_birth is None


def test_create_race_from_dict():
    race = {
        'race_name': 'Biegnij Warszawo',
        'race_date': '2018-10-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1997',
        'result_of_the_race': '00:39:12'
    }
    race_result = RaceResult(**race)
    assert race_result.race_name == 'Biegnij Warszawo'
    assert race_result.race_date == datetime.date(2018, 10, 11)
    assert race_result.distance == 10.0
    assert race_result.race_type == 'bieganie'
    assert race_result.runner_birth == 1997
    assert race_result.result_of_the_race == datetime.timedelta(
        hours=0, minutes=39, seconds=12)


def test_equality():
    race_result1 = {
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    }
    race_result2 = {
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    }
    race_result3 = {
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '10 km',
        'race_type': 'Bieganie Górskie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    }
    race1 = RaceResult(**race_result1)
    race2 = RaceResult(**race_result2)
    race3 = RaceResult(**race_result3)
    assert race1 == race2
    assert race2 != race3
