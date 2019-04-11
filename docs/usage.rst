=====
Usage
=====

To use Running Results Fetcher in a project::

    
    from running_results_fetcher import RunningResultFetcher
    fetcher = RunningResultFetcher('Michał Mojek', 1980)

    # now you have to run a spider and fetch data
    # this will return a runner
    runner=fetcher.fetch_data_for_runner()

    # If you want you can filter races on the runner.
    # All this are optional.
    # race_type can be: 'Biegi Górskie' or 'Bieganie'.
    runner.filter_races(from_date="2018-11-10",
                         to_date="2019-11-10",
                         race_type="Bieganie")
    #or                         
    runner.filter_races( to_date="2019-11-10",
                         race_type="Bieganie")
    #or
    runner.filter_races(race_type="Bieganie")                                                  

    
    
    # and now you can get statistics

    # The number of kilometers in all races
    runner.stats.km_count() 
     
    # You can get the best time at a given distance. 
    # You can also enter a 'maraton',
    # or polmaraton
    runner.stats.best_time_on_distance('10 km'))
    runner.stats.best_time_on_distance('maraton'))
    runner.stats.best_time_on_distance(20))
    
    # Returns the longest run
    runner.stats.longest_run()
