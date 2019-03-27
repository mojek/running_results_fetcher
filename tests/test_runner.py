from running_results_fetcher.runner import Runner


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
