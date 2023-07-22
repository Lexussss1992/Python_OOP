import unittest

from project.mammal import Mammal


class TestMammalClass(unittest.TestCase):
    def test_init(self):

        #Act

        mammal = Mammal('Ivo', 'human', 'speak')

        #Assert

        self.assertEqual('Ivo', mammal.name)
        self.assertEqual('human', mammal.type)
        self.assertEqual('speak', mammal.sound)

    def test_making_sound(self):
        mammal = Mammal('Ivo', 'human', 'speak')

        self.assertEqual('Ivo makes speak', mammal.make_sound())

    def test_info(self):
        mammal = Mammal('Ivo', 'human', 'speak')

        self.assertEqual('Ivo is of type human', mammal.info())

    def test_get_kingdom(self):
        mammal = Mammal('Ivo', 'human', 'speak')

        self.assertEqual('animals', mammal.get_kingdom())


if __name__ == '__main__':
    unittest.main()