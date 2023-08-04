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
        found_jockey_flag = False
        found_horse_flag = False
        taken_horse_flag = False

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                found_jockey_flag = True

        if not found_jockey_flag:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                found_horse_flag = True

        for horse in self.horses:
            if horse.__class__.__name__ == horse_type and horse.is_taken is True:
                taken_horse_flag = True

        if not found_horse_flag and not taken_horse_flag:
            raise f'Horse breed {horse_type} could not be found!'

        jockey = [j for j in self.jockeys if j.name == jockey_name][0]

        for horse in self.horses:
            if horse.__class__.__name__ == horse_type and horse.is_taken is False and jockey.horse is None:
                jockey.horse = horse
                return f'Jockey {jockey_name} will ride the horse {horse.name}.'
            elif horse.__class__.__name__ == horse_type and horse.is_taken is False and jockey.horse is not None:
                return f'Jockey {jockey_name} already has a horse.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        found_race_flag = False
        found_jockey_flag = False

        for race in self.horse_races:
            if race.race_type == race_type:
                found_race_flag = True

        if not found_race_flag:
            raise Exception(f'Race {race_type} could not be found!')

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                found_jockey_flag = True

        if not found_jockey_flag:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        jockey = [j for j in self.jockeys if j.name == jockey_name][0]

        if not jockey.horse:
            raise Exception(F'Jockey {jockey_name} cannot race without a horse!')

        if jockey in self.horse_races:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'

        for race in self.horse_races:
            if race.race_type == race_type:
                race.jockeys.append(jockey)

        return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type: str):
        horse_race_flag = False

        for race in self.horse_races:
            if race.race_type == race_type:
                horse_race_flag = True

        if not horse_race_flag:
            raise Exception(f'Race {race_type} could not be found!')

        for race in self.horse_races:
            if race.race_type == race_type:
                if len(race.jockeys) < 2:
                    raise Exception(f'Horse race {race_type} needs at least two participants!')

        winner = None
        speed = 0
        horse_name = None

        race = [r for r in self.horse_races if r.race_type == race_type][0]

        for jockey in self.jockeys:
            if jockey.horse.speed > speed:
                speed = jockey.horse.speed
                winner = jockey
                horse_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {speed}km/h is {winner.name}! Winner's horse: {horse_name}."


# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))