from .race_result import RaceResult
from .stats import Stats


class Runner:
    "A class represents a Runner"

    def __init__(self, name, birth):
        """
        Arguments:
            name {str} -- name and surname of the runner
            birth {str} --the year of birth of a runner
        """

        self.name = name
        self.birth = birth
        self.race_results = []
        self.stats = None

    def add_races(self, races):
        """
        Add a race list to the runner.

        A single race is in the form of a dictionary.
        The race is added to the runner if it meets the specified conditions.
        A RaceResult object is created from a single dictionary.

        Arguments:
            races(list): List of dictionaries, dictionary
                has keys: race_name, distance, race_date,
                runner_birth, result_of_the_race, race_type
        """

        for race in races:
            race_result = RaceResult(**race)
            if self.__can_add_race(race_result):
                self.race_results.append(race_result)

    def filter_races(self, **kwargs):
        """The method creates a stats object and returns filtered results.

         Arguments:
             kwargs : Arguments used to create the object Stats

         """

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
        if not race_result.distance:
            return False
        if not race_result.result_of_the_race:
            return False
        if not race_result.runner_birth == self.birth:
            return False
        if race_result in self.race_results:
            return False
        return True
