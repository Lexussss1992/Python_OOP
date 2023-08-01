from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):

    def setUp(self) -> None:
        self.robot = Robot('123', 'Military', 10, 100)

    def test_class_atr(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_valid_init(self):
        self.assertEqual('123', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            Robot('123', 'Test', 10, 100)
        self.assertEqual(str(ve.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as ve:
            Robot('123', 'Military', 10, -1)
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade_if_hardware_component_in_hardware_upgrades(self):
        self.robot.hardware_upgrades.append('test')

        self.assertEqual(self.robot.upgrade('test', 10), "Robot 123 was not upgraded.")

    def test_upgrade_if_hardware_component_not_in_hardware_upgrades(self):
        res = self.robot.upgrade('test', 10)

        self.assertEqual(['test'], self.robot.hardware_upgrades)
        self.assertEqual(115, self.robot.price)
        self.assertEqual('Robot 123 was upgraded with test.', res)

    def test_update_if_aval_capacity_less_than_needed_capacity(self):
        res = self.robot.update(1, 20)

        self.assertEqual("Robot 123 was not updated.", res)

    def test_update_if_self_software_updates_and_version_less_than_or_equal_max_self_software_updates(self):
        self.robot.software_updates.append(10)
        self.robot.software_updates.append(15)

        res = self.robot.update(12, 5)

        self.assertEqual("Robot 123 was not updated.", res)

    def test_update_if_aval_capacity_greater_than_needed_capacity(self):
        res = self.robot.update(1, 5)

        self.assertEqual([1], self.robot.software_updates)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual('Robot 123 was updated to version 1.', res)

    def test_update_if_not_self_software_updates_and_version_greater_than_max_self_software_updates(self):
        self.robot.software_updates.append(10)
        self.robot.software_updates.append(15)

        res = self.robot.update(20, 5)

        self.assertEqual([10, 15, 20], self.robot.software_updates)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual('Robot 123 was updated to version 20.', res)

    def test_str_if_self_price_greater_than_other_price(self):
        res = self.robot.__gt__(Robot('456', 'Education', 10, 50))

        self.assertEqual('Robot with ID 123 is more expensive than Robot with ID 456.', res)

    def test_str_if_self_price_equal_other_price(self):
        res = self.robot.__gt__(Robot('456', 'Education', 10, 100))

        self.assertEqual('Robot with ID 123 costs equal to Robot with ID 456.', res)

    def test_str_if_self_price_less_than_other_price(self):
        res = self.robot.__gt__(Robot('456', 'Education', 10, 150))

        self.assertEqual('Robot with ID 123 is cheaper than Robot with ID 456.', res)

if __name__ == '__main__':
    main()