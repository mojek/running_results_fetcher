class FetcherManager:
    """This class manage all functionality of the package"""

    def __init__(self):
        self.runners = []

    def add_runner(self, runner):
        """Add runner to Fetcher Manager"""
        self.runners.append(runner)
