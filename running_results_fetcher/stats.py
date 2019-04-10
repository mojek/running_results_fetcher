from datetime import datetime, timedelta
from .helpers import string_to_date
from .helpers import convert_distance


class Stats:
    """It's calculate statistics for the runner"""

    def __init__(self, runner, **kwargs):
        self.runner = runner
        self.from_date = kwargs.get('from_date')
        self.to_date = kwargs.get('to_date')
        self.race_type = kwargs.get('race_type')
        self.race_results = self.__filter_race()

    def km_count(self):
        return sum(race.distance for race in self.race_results)

    def best_time_on_distance(self, distance):
        conv_distance = convert_distance(distance)
        filter_race_with_disntace = [
            race for race in self.race_results
            if race.distance == conv_distance]

        if not filter_race_with_disntace:
            raise ValueError("Runner don't have race results")

        best_result = min(filter_race_with_disntace,
                          key=lambda race: race.result_of_the_race,
                          )

        return best_result.result_of_the_race

    def longest_run(self):
        if not self.race_results:
            raise ValueError("Runner don't have race results")
        return max(race.distance for race in self.race_results)

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

    def __filter_race(self):
        list_of_races = self.runner.race_results
        from_date = self.from_date
        to_date = self.to_date
        race_type = self.race_type

        from_date = from_date or \
            (datetime.now() - timedelta(days=100*365)).date()

        to_date = to_date or datetime.now().date()

        return [race for race in list_of_races
                if from_date <= race.race_date <= to_date and
                (
                    (race.race_type and race.race_type == race_type)
                    or race_type is None)
                ]
