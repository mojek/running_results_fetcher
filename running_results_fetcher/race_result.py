class RaceResult:
    def __init__(self, race_name):
        self.race_name = race_name

    @property
    def race_name(self):
        return self.__race_name

    @race_name.setter
    def race_name(self, race_name):
        race_name = " ".join(race_name.split())
        self.__race_name = race_name
