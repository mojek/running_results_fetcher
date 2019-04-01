from .race_result import RaceResult


class Runner:
    """class that represents the runner"""

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.race_results = []

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

    def add_races(self, races):
        for race in races:
            race_result = RaceResult(**race)
            if race_result.runner_birth == self.birth:
                self.race_results.append(race_result)
