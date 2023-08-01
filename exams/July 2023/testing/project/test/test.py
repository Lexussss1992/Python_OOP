import unittest

from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):
    def test_init(self):
        tennis_player = TennisPlayer('Ivo', 31, 100)

        self.assertEqual('Ivo', tennis_player.name)
        self.assertEqual(31, tennis_player.age)
        self.assertEqual(100, tennis_player.points)
        self.assertEqual([], tennis_player.wins)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('Iv', 19, 100)
        self.assertEqual(str(ve.exception), 'Name should be more than 2 symbols!')

    def test_invalid_age(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('Ivo', 17, 100)
        self.assertEqual(str(ve.exception), 'Players must be at least 18 years of age!')

    def test_invalid_name_and_age(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('Iv', 17, 100)

    def test_add_new_win_without_tournament_name(self):
        tennis_player = TennisPlayer('Ivo', 31, 100)

        tennis_player.add_new_win('Wimbledon')
        tennis_player.add_new_win('US Open')

        self.assertEqual(['Wimbledon', 'US Open'], tennis_player.wins)

    def test_add_new_win_with_tournament_name(self):
        tennis_player = TennisPlayer('Ivo', 31, 100)

        tennis_player.add_new_win('Wimbledon')
        tennis_player.add_new_win('US Open')

        self.assertEqual(tennis_player.add_new_win('Wimbledon'), "Wimbledon has been already added to the list of wins!")

    def test_lt_self_points_less_than_other_player(self):
        tennis_player = TennisPlayer('Ivo', 31, 100)
        other_tennis_player = TennisPlayer('Pesho', 31, 110)

        self.assertEqual(tennis_player.__lt__(other_tennis_player), 'Pesho is a top seeded player and he/she is better than Ivo')

    def test_lt_self_points_greater_than_other_player(self):
        tennis_player = TennisPlayer('Ivo', 31, 100)
        other_tennis_player = TennisPlayer('Pesho', 31, 90)

        self.assertEqual(tennis_player.__lt__(other_tennis_player), 'Ivo is a better player than Pesho')

    def test_lt_self_points_equal_to_other_player(self):
        tennis_player = TennisPlayer('Ivo', 31, 100)
        other_tennis_player = TennisPlayer('Pesho', 31, 100)

        self.assertEqual(tennis_player.__lt__(other_tennis_player), 'Ivo is a better player than Pesho')

    def test_str(self):
        tennis_player = TennisPlayer('Ivo', 31, 100)
        tennis_player.add_new_win('Wimbledon')
        tennis_player.add_new_win('US Open')

        res = "Tennis Player: Ivo\n" \
              "Age: 31\n" \
              "Points: 100.0\n" \
              "Tournaments won: Wimbledon, US Open"

        self.assertEqual(res, tennis_player.__str__())


if __name__ == '__main__':
    unittest.main()
