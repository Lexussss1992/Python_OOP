from unittest import TestCase

from project.mammal import Mammal


class TestMammalClass(TestCase):
    def setUp(self) -> None:
        mammal == Mammal('Ivo', 'human', 'speak')