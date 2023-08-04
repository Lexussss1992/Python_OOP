from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_TYPES_HORSE_BREEDS = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type in self.VALID_TYPES_HORSE_BREEDS:
            self.horses.append(self.VALID_TYPES_HORSE_BREEDS[horse_type](horse_name, horse_speed))
            return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f'Jockey {jockey_name} has been already added!')

        self.jockeys.append(Jockey(jockey_name, age))
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):

        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f'Race {race_type} has been already created!')

        self.horse_races.append(HorseRace(race_type))
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        for jockey in self.jockeys:
            if jockey.name != jockey_name:
                raise Exception(f'Jockey {jockey_name} could not be found!')

        if horse_type not in self.VALID_TYPES_HORSE_BREEDS:
            raise f'Horse breed {horse_type} could not be found!'

        jockey = [j for j in self.jockeys if j.name == jockey_name][0]

        for horse in self.horses:
            if horse.__class__.__name__ == horse_type and horse.is_taken is False and jockey.horse is None:
                return f'Jockey {jockey_name} will ride the horse {horse.name}.'
            elif horse.__class__.__name__ == horse_type and horse.is_taken is False and jockey.horse is not None:
                return f'Jockey {jockey_name} already has a horse.'
