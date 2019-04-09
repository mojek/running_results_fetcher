import pytest
from running_results_fetcher.runner import Runner
from running_results_fetcher.race_result import RaceResult


def test_setting_runner():
    runner = Runner("Michal Mojek", 1980)
    assert runner.name == 'Michal Mojek'
    assert runner.birth == 1980


def test_setting_runner_birth_with_string():
    runner = Runner("Michal Mojek", "1980")
    assert runner.birth == 1980


def test_setting_runner_birth_with_short_string():
    runner = Runner("Michal Mojek", "80")
    assert runner.birth == 1980


def test_setting_runner_birth_with_short_int():
    runner = Runner("Michal Mojek", 80)
    assert runner.birth == 1980


def test_setting_runner_name_with_onclean_data():
    runner = Runner("Michal   Mojek ", 1980)
    assert runner.name == 'Michal Mojek'


def test_add_mass_races_add_only_with_the_same_birth_year():
    runner = Runner("Michal Mojek", 80)
    races = [{
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    },
        # wrong_runner_birth
        {
        'race_name': 'Biegnij Warszawo',
        'race_date': '2018-10-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1997',
        'result_of_the_race': '00:39:12'
    },
        # no runner birth
        {
        'race_name': 'Biegnij Warszawo',
        'race_date': '2018-10-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '',
        'result_of_the_race': '00:39:12'
    }
    ]
    runner.add_races(races)
    assert isinstance(runner.race_results[0], RaceResult)
    assert len(runner.race_results) == 1


def test_uniqness_off_the_race():
    runner = Runner("Michal Mojek", 80)
    # same name and same date
    races = [{
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    },
        {
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    },
    ]
    runner.add_races(races)
    assert isinstance(runner.race_results[0], RaceResult)
    assert len(runner.race_results) == 1


def test_dont_add_run_without_distance():
    runner = Runner("Michal Mojek", 80)
    # same name and same date
    races = [{
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '-',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    },
        {
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    },
    ]
    runner.add_races(races)
    assert len(runner.race_results) == 1


def test_dont_add_run_without_result_of_the_race():
    runner = Runner("Michal Mojek", 80)
    # same name and same date
    races = [{
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': 'maraton',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '-'
    },
        {
        'race_name': 'Bieg Niepodległości',
        'race_date': '2018-11-11',
        'distance': '10 km',
        'race_type': 'bieganie',
        'runner_birth': '1980',
        'result_of_the_race': '00:39:12'
    },
    ]
    runner.add_races(races)
    assert len(runner.race_results) == 1


def test_best_time_on_distance():
    runner = Runner("Michal Mojek", 80)
    race_4 = race_dict(race_date='2018-11-11',
                       distance="10 km", result_of_the_race='00:39:12')
    race_2 = race_dict(race_date='2018-11-11',
                       distance="10 km", result_of_the_race='00:39:12')
    race_1 = race_dict(race_date='2018-10-11',
                       distance="10 km", result_of_the_race='00:49:12')
    race_3 = race_dict(race_date='2018-09-11',
                       distance="21 km", result_of_the_race='00:09:12')
    race_5 = race_dict(race_date='2018-09-11',
                       distance="21 km", result_of_the_race='00:25:12',
                       race_type="Bieganie górskie")
    race_6 = race_dict(race_date='2018-09-12',
                       distance="21 km", result_of_the_race='01:30:12',
                       race_type="Bieganie górskie")
    runner.add_races([race_1, race_2, race_4, race_3,  race_5, race_6])

    runner.filter_races(race_type="Bieganie")
    assert str(runner.stats.best_time_on_distance(10.0)) == '0:39:12'

    assert str(runner.stats.best_time_on_distance("10 km")) == '0:39:12'

    runner.filter_races(race_type="Bieganie górskie")
    assert str(runner.stats.best_time_on_distance(21)) == '0:25:12'


def test_best_time_on_distance_value_error_when_no_run():
    runner = Runner("Michal Mojek", 80)
    with pytest.raises(ValueError):
        runner.stats.best_time_on_distance('10 km')


def test_longest_run_value_error_when_no_run():
    runner = Runner("Michal Mojek", 80)
    with pytest.raises(ValueError):
        runner.stats.longest_run()


def test_km_count():
    runner = Runner("Michal Mojek", 80)
    races = []
    races.append(race_dict(race_date='2018-11-11', distance="50 km"))
    races.append(race_dict(race_date='2018-11-12', distance="20 km"))
    races.append(race_dict(race_date='2018-11-13', distance="2 km"))
    races.append(race_dict(race_date='2018-11-14', distance="1 km"))
    races.append(race_dict(race_date='2018-11-14',
                           distance="5 km", race_type="Bieganie górskie"))
    runner.add_races(races)
    runner.filter_races(race_type="Bieganie")
    assert runner.stats.km_count() == 73
    assert runner.stats.km_count() == 73


def test_longest_run():
    runner = Runner("Michal Mojek", 80)
    races = []
    races.append(race_dict(race_date='2018-11-11', distance="50 km"))
    races.append(race_dict(race_date='2018-11-12', distance="20 km"))
    races.append(race_dict(race_date='2018-11-13', distance="2 km"))
    races.append(race_dict(race_date='2018-11-14', distance="1 km"))
    races.append(race_dict(race_date='2018-11-14',
                           distance="500 km", race_type="Bieganie górskie"))
    runner.add_races(races)
    runner.filter_races(race_type="Bieganie")
    assert runner.stats.longest_run() == 50


def test_longest_run_no_filter():
    runner = Runner("Michal Mojek", 80)
    races = []
    races.append(race_dict(race_date='2018-11-11', distance="50 km"))
    races.append(race_dict(race_date='2018-11-12', distance="20 km"))
    races.append(race_dict(race_date='2018-11-13', distance="2 km"))
    races.append(race_dict(race_date='2018-11-14', distance="1 km"))
    races.append(race_dict(race_date='2018-11-14',
                           distance="500 km", race_type="Bieganie górskie"))
    runner.add_races(races)
    assert runner.stats.longest_run() == 500


def test_km_count_without_filter():
    runner = Runner("Michal Mojek", 80)
    races = []
    races.append(race_dict(race_date='2018-11-11', distance="10 km"))
    races.append(race_dict(race_date='2018-11-12', distance="23 km"))
    races.append(race_dict(race_date='2018-11-13', distance="15 km"))
    races.append(race_dict(race_date='2018-11-14', distance="15 km"))
    races.append(race_dict(race_date='2018-11-14',
                           distance="15 km", race_type="Bieganie górskie"))
    runner.add_races(races)
    assert runner.stats.km_count() == 78


def test_filter_races_by_race_type():
    runner = Runner("Michal Mojek", 80)
    races = []
    races.append(race_dict(race_date='2018-11-11', distance="10 km"))
    races.append(race_dict(race_date='2018-11-12', distance="23 km"))
    races.append(race_dict(race_date='2018-11-14',
                           distance="15 km", race_type="Bieganie górskie"))
    runner.add_races(races)
    assert len(list(runner.filter_races(race_type="Bieganie"))) == 2


def test_filter_races_by_from_date():
    runner = Runner("Michal Mojek", 80)
    races = []
    races.append(race_dict(race_date='2018-11-11', distance="10 km"))
    races.append(race_dict(race_date='2018-11-12', distance="23 km"))
    races.append(race_dict(race_date='2018-11-14',
                           distance="15 km", race_type="Bieganie górskie"))
    runner.add_races(races)
    assert len(list(runner.filter_races(from_date="2018-11-12"))) == 2
    assert len(list(runner.filter_races(from_date="2018-11-14"))) == 1
    assert len(list(runner.filter_races(from_date="2017-11-14"))) == 3


def test_filter_races_by_from_date_to_date():
    runner = Runner("Michal Mojek", 80)
    races = []
    races.append(race_dict(race_date='2018-11-11', distance="10 km"))
    races.append(race_dict(race_date='2018-11-12', distance="23 km"))
    races.append(race_dict(race_date='2018-11-14',
                           distance="15 km", race_type="Bieganie górskie"))
    runner.add_races(races)
    assert len(list(runner.filter_races(
        from_date="2018-11-12", to_date="2018-11-12"))) == 1


def test_filter_races_by_from_date_to_date_race_type():
    runner = Runner("Michal Mojek", 80)
    races = []
    races.append(race_dict(race_date='2018-11-11', distance="10 km"))
    races.append(race_dict(race_date='2018-11-12', distance="23 km"))
    races.append(race_dict(race_date='2018-11-13', distance="15 km"))
    races.append(race_dict(race_date='2018-11-14', distance="15 km"))
    races.append(race_dict(race_date='2018-11-14',
                           distance="15 km", race_type="Bieganie górskie"))
    runner.add_races(races)
    assert len(list(runner.filter_races(
        from_date="2018-11-11",
        to_date="2018-11-20",
        race_type="Bieganie"))) == 4


def race_dict(**kwargs):
    race_name = kwargs.get('race_name', 'Biegnij Warszawo')
    race_date = kwargs.get('race_date', '2017-10-11')
    distance = kwargs.get('distance', '10km')
    race_type = kwargs.get('race_type', 'Bieganie')
    runner_birth = kwargs.get('runner_birth', '1980')
    result_of_the_race = kwargs.get('result_of_the_race', '00:36:12')
    race = {
        'race_name': race_name,
        'race_date': race_date,
        'distance': distance,
        'race_type': race_type,
        'runner_birth': runner_birth,
        'result_of_the_race': result_of_the_race
    }
    return race
