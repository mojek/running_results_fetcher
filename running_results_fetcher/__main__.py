# """Console script for running_results_fetcher."""
# import sys
# import click

# from .runner import Runner
# from .spider_config import SpiderConfig
# from .running_results_fetcher import RunningResultFetcher
# @click.command()
# @click.option('--runner', prompt='Runner name')
# @click.option('--birth', prompt='Birth year')
# def main(runner, birth):
#     rrf = RunningResultFetcher()
#     runner = Runner(runner, birth)
#     config = SpiderConfig(domain_name='enduhub.com')
#     config.runner = runner
#     config.url_suffix = "/pl/search/?name={}&page=1".format(runner.name)
#     selctor = '.pagination .pages .active + li a::attr(href)'
#     config.next_page_selector = selctor
#     rrf.set_spider_config(config)
#     rrf.fetch_data_for_runner()
#     try:
#         click.echo("runner longest_run: " + str(runner.stats.longest_run()))

#         click.echo("runner km_count: " + str(runner.stats.km_count()))
#         click.echo("runner best_time_on_10km: " +
#                    str(runner.stats.best_time_on_distance(10)))
#         click.echo("runner best_time_on_maraton: " +
#                    str(runner.stats.best_time_on_distance('maraton')))
#     except ValueError:
#         click.echo("Race results not found")

#     return 0


# if __name__ == "__main__":
#     sys.exit(main())  # pragma: no cover
