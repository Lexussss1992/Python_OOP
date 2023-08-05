class Player:
    PLAYERS_CREATED = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self._need_substance = True if stamina < 100 else None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Name not valid!')
        elif value in self.PLAYERS_CREATED:
            raise ValueError(f'Name {value} is already used!')
        self.PLAYERS_CREATED.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError('The player cannot be under 12 years old!')
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError('Stamina not valid!')
        self.__stamina = value

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self._need_substance}'
