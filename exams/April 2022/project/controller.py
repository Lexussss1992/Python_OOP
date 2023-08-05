from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_SUSTENANCE_FOOD = [
        'Food',
        'Drink'
    ]

    ADDED_PLAYERS = []

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    @staticmethod
    def find_player(players, name):
        for player in players:
            if player.name == name:
                return player

    def add_player(self, *players):

        for p in players:
            if p not in self.players:
                self.players.append(p)
                self.ADDED_PLAYERS.append(p)

        res = "Successfully added: " + f"{', '.join([p.name for p in self.ADDED_PLAYERS])}"
        added_players = []
        return res

    def add_supply(self, *supplies):

        for s in supplies:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):

        try:
            player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return

        if sustenance_type not in self.VALID_SUSTENANCE_FOOD:
            return

        if sustenance_type == 'Food':
            try:
                food = next(filter(lambda x: x.__class__.__name__ == sustenance_type, self.supplies))
            except StopIteration:
                raise Exception(f'There are no food supplies left!')

        if sustenance_type == 'Drink':
            try:
                drink = next(filter(lambda x: x.__class__.__name__ == sustenance_type, self.supplies))
            except StopIteration:
                raise Exception(f'There are no drink supplies left!')

        if player.stamina == 100:
            return f'{player_name} have enough stamina.'

        supp = self.supplies[::-1]
        for supply in supp:
            if supply.__class__.__name__ == sustenance_type:
                if supply.energy + player.stamina > 100:
                    player.stamina = 100
                else:
                    player.stamina += supply.energy

                supp.remove(supply)
                self.supplies = supp[::-1]
                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        res = []

        try:
            player_one = next(filter(lambda x: x.name == first_player_name and x.stamina > 0, self.players))
        except:
            res.append(f'Player {first_player_name} does not have enough stamina.')

        try:
            player_two = next(filter(lambda x: x.name == second_player_name and x.stamina > 0, self.players))
        except:
            res.append(f'Player {second_player_name} does not have enough stamina.')

        if res:
            return "\n".join(res)

        player_one = next(filter(lambda x: x.name == first_player_name, self.players))
        player_two = next(filter(lambda x: x.name == second_player_name, self.players))

        if player_one.stamina < player_two.stamina:
            player_two.stamina -= player_one.stamina / 2
            if player_two.stamina <= 0:
                player_two.stamina = 0
                return f'Winner: {player_one.name}'
        elif player_two.stamina < player_one.stamina:
            player_one.stamina -= player_two.stamina / 2
            if player_one.stamina <= 0:
                player_one.stamina = 0
                return f'Winner: {player_two.name}'

        if player_one.stamina < player_two.stamina:
            return f'Winner: {player_two.name}'
        elif player_two.stamina < player_one.stamina:
            return f'Winner: {player_one.name}'

    def next_day(self):
        for player in self.players:
            if player.stamina - (2 * player.age) < 0:
                player.stamina = 0
            else:
                player.stamina -= (2 * player.age)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())
        return "\n".join(result)