from running_results_fetcher.runner import Runner


def test_setting_runner_name_by_init():
    runner = Runner("Michal Mojek")
    assert runner.name == 'Michal Mojek'
