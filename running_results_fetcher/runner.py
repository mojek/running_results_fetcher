from .race_result import RaceResult


class Runner:
    """class that represents the runner"""

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.race_results = []

    def best_time_on_distance(self, distance, race_type, from_date, to_date):
        # TODO best time on distance
        pass

    def km_count(self, race_type, from_date, to_date):
        # TODO km count
        pass

    def longest_run(self, race_type, from_date, to_date):
        # TODO longest run
        pass

    def add_races(self, races):
        for race in races:
            race_result = RaceResult(**race)
            if self.__can_add_race(race_result):
                self.race_results.append(race_result)

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
