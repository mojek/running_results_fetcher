from .helpers import string_to_date


class Stats:
    """It's calculate statistics for the runner"""

    def __init__(self, runner, **kwargs):
        self.runner = runner
        self.from_date = kwargs.get('from_date')
        self.to_date = kwargs.get('to_date')
        self.race_type = kwargs.get('race_type')

    @property
    def from_date(self):
        return self.__from_date

    @from_date.setter
    def from_date(self, from_date):
        self.__from_date = from_date
        if from_date:
            self.__from_date = string_to_date(from_date)

    @property
    def to_date(self):
        return self.__to_date

    @to_date.setter
    def to_date(self, to_date):
        self.__to_date = to_date
        if to_date:
            self.__to_date = string_to_date(to_date)
