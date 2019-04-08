import datetime
from .race_result import RaceResult
from .stats import Stats


class Runner:
    """class that represents the runner"""

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.race_results = []
        self.stats = None
    # make new class statictics with params from date to date race type

    def add_races(self, races):
        for race in races:
            race_result = RaceResult(**race)
            if self.__can_add_race(race_result):
                self.race_results.append(race_result)

    def filter_races(self, **kwargs):
        stats = Stats(self, **kwargs)
        self.stats = stats
        return stats.race_results

    @property
    def stats(self):
        if self.__stats:
            return self.__stats
        else:
            return Stats(self)

    @stats.setter
    def stats(self, stats):
        self.__stats = stats

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name = " ".join(name.split())
        self.__name = name

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, birth):
        if len(str(birth)) == 2:
            birth = "19"+str(birth)
        self.__birth = int(birth)

    def __can_add_race(self, race_result):
        if not race_result.runner_birth == self.birth:
            return False
        if race_result in self.race_results:
            return False
        return True
