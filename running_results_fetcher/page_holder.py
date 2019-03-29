from running_results_fetcher.race_result import RaceResult


class PageHolder:
    """It' take care of downloaded page"""

    def __init__(self, raw_html):
        self.raw_html = raw_html
        self.race_results = []

    def parse_page(self):
        [self.race_results.append(RaceResult()) for race in range(27)]
