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
