from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Ivo', 5, 5.5, 55.5)

    def test_init(self):
        self.assertEqual('Ivo', self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(5.5, self.hero.health)
        self.assertEqual(55.5, self.hero.damage)

    def test_if_names_are_equal(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero('Ivo', 5, 5.5, 55.5))

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_if_self_health_hero_equal_to_zero(self):
        self.hero = Hero('Ivo', 5, 0, 55.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero('Pesho', 5, 5.5, 55.5))

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_if_self_health_hero_less_than_zero(self):
        self.hero = Hero('Ivo', 5, -1, 55.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero('Pesho', 5, 5.5, 55.5))

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_if_enemy_health_hero_less_than_zero(self):
        self.hero = Hero('Ivo', 5, 5.5, 55.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero('Pesho', 5, -1, 55.5))

        self.assertEqual('You cannot fight Pesho. He needs to rest', str(ex.exception))

    def test_if_enemy_health_hero_equal_to_zero(self):
        self.hero = Hero('Ivo', 5, 5.5, 55.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero('Pesho', 5, 0, 55.5))

        self.assertEqual('You cannot fight Pesho. He needs to rest', str(ex.exception))

    def test_if_self_hero_win(self):
        self.hero.battle(Hero('Pesho', 1, 1, 1))

        self.assertEqual(6, self.hero.level)
        self.assertEqual(9.5, self.hero.health)
        self.assertEqual(60.5, self.hero.damage)
        self.assertTrue('You win', self.hero.battle(Hero('Pesho', 1, 1, 1)))

if __name__ == '__main__':
    main()