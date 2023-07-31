from unittest import TestCase, main

from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)
        with self.assertRaises(ValueError) as ex:
            Plantation(-1)

    def test_hire_worker_already_hired(self):
        self.plantation.workers.append('Ivo')
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker('Ivo')

    def test_hire_new_worker(self):
        Plantation(10).workers.append('Ivo')
        self.assertEqual("Ivo successfully hired.", self.plantation.hire_worker('Ivo'))

    def test__len__(self):
        self.assertEqual(0, self.plantation.__len__())

    def test_planting_if_worker_not_hired(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Ivo', 'Roza')

    def test_if_self_len_greater_than_or_equal_than_self_size(self):
        self.plantation = Plantation(1)
        self.plantation.hire_worker('Ivo')
        self.plantation.planting('Ivo', 'Roza')
        self.plantation.hire_worker('Pesho')
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Ivo', 'Lale')

    def test_if_worker_in_plants_keys(self):
        self.plantation = Plantation(10)
        self.plantation.hire_worker('Ivo')
        self.plantation.planting('Ivo', 'Roza')
        self.assertEqual("Ivo planted Roza.", self.plantation.planting('Ivo', 'Roza'))

    def test_if_worker_is_hired_and_not_in_plants_keys(self):
        self.plantation = Plantation(10)
        self.plantation.hire_worker('Ivo')
        self.assertEqual("Ivo planted it's first Roza.", self.plantation.planting('Ivo', 'Roza'))

    def test_str(self):
        self.plantation.hire_worker('Ivo')
        self.plantation.hire_worker('Pesho')
        self.plantation.planting('Ivo', 'Roza')
        self.plantation.planting('Pesho', 'Lale')
        res = "Plantation size: 10\n" \
              "Ivo, Pesho\n" \
              "Ivo planted: Roza\n" \
              "Pesho planted: Lale"

        self.assertEqual(res, self.plantation.__str__())

    def test_repr(self):
        self.plantation.hire_worker('Ivo')
        self.plantation.hire_worker('Pesho')
        res = 'Size: 10\n' \
              'Workers: Ivo, Pesho'

        self.assertEqual(res, self.plantation.__repr__())


if __name__ == '__main__':
    main()