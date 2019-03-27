class Runner:
    """class that represents the runner"""

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, birth):
        self.__birth = int(birth)
