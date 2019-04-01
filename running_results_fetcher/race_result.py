class RaceResult:
    def __init__(self, **kargs):
        self.race_name = kargs.get('race_name', '')
        self.distance = kargs.get('distance')

    @property
    def race_name(self):
        return self.__race_name

    @race_name.setter
    def race_name(self, race_name):
        race_name = " ".join(race_name.split())
        self.__race_name = race_name

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance):
        if distance is None or distance is float:
            self.__distance = distance
            return
        import re
        result = distance
        if isinstance(distance, str):
            if distance.lower() == "maraton":
                result = 42.1
            elif distance.lower() == "półmaraton":
                result = 21.05
            else:
                find_digit = re.match(r"\d*", distance)
                result = find_digit.group()

        self.__distance = float(result)
