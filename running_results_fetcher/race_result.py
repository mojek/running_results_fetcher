from datetime import datetime
from datetime import timedelta
from .helpers import convert_distance


class RaceResult:
    def __init__(self, **kwargs):
        self.race_name = kwargs.get('race_name', '')
        self.distance = kwargs.get('distance')
        self.runner_birth = kwargs.get('runner_birth')
        self.race_date = kwargs.get('race_date')
        self.race_type = kwargs.get('race_type')
        self.result_of_the_race = kwargs.get('result_of_the_race')

    def __eq__(self, other):
        if not self.race_type == other.race_type:
            return False
        if not self.race_name == other.race_name:
            return False
        if not self.distance == other.distance:
            return False
        if not self.race_date == other.race_date:
            return False
        return True

    def __str__(self):
        return "{}{}{}".format(self.race_name, self.distance,
                               self.result_of_the_race)

    def __repr__(self):
        return "{} {}".format(self.race_type, self.result_of_the_race)

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
        self.__distance = convert_distance(distance)

    @property
    def runner_birth(self):
        return self.__runner_birth

    @runner_birth.setter
    def runner_birth(self, runner_birth):
        if not runner_birth:
            self.__runner_birth = None
            return None

        if len(str(runner_birth)) == 2:
            runner_birth = "19"+str(runner_birth)

        try:
            self.__runner_birth = int(runner_birth)
        except ValueError:
            self.__runner_birth = None

    @property
    def race_date(self):
        return self.__race_date

    @race_date.setter
    def race_date(self, string_date):
        """Parse string and change to date"""
        if not string_date:
            self.__race_date = None
            return None
        string_date = datetime.strptime(string_date, '%Y-%m-%d')
        self.__race_date = string_date.date()

    @property
    def result_of_the_race(self):
        return self.__result_of_the_race

    @result_of_the_race.setter
    def result_of_the_race(self, string_time):
        """Parse string and change to time delta"""
        if not string_time:
            return None
        ti = string_time.split(':')
        try:
            hour = int(ti[0])
            minute = int(ti[1])
            second = int(ti[2])
        except ValueError:
            time_delta = None
        except IndexError:
            time_delta = None
        else:
            time_delta = timedelta(hours=hour, minutes=minute, seconds=second)
        self.__result_of_the_race = time_delta
