import datetime
from .race_result import RaceResult
from .stats import Stats


class Runner:
    """class that represents the runner"""

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.race_results = []
        self.stats = Stats(self)
    # make new class statictics with params from date to date race type

    def best_time_on_distance(self, distance):
        """Return best time on given distance"""
        stats = self.stats
        return stats.best_time_on_distance(10)

    def km_count(self):
        stats = self.stats
        return stats.km_count()

    def longest_run(self, race_type, **kwargs):
        # TODO longest run
        pass

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

    @staticmethod
    def __filter_race(list_of_races, race_type,
                      from_date=None, to_date=None):
        if from_date:
            from_date = datetime.datetime.strptime(
                from_date, '%Y-%m-%d').date()
        if to_date:
            to_date = datetime.datetime.strptime(
                to_date, '%Y-%m-%d').date()

        from_date = from_date or \
            (datetime.datetime.now() - datetime.timedelta(days=100*365)).date()

        to_date = to_date or datetime.datetime.now().date()
        return (race for race in list_of_races
                if race.race_type == race_type
                and from_date <= race.race_date <= to_date)
