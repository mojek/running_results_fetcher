

def test_add_runner_to_fetcher_manager(runner, fetcher_manager):
    fetcher_manager.add_runner(runner)
    assert len(fetcher_manager.runners) == 1
