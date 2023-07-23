import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def test_init(self):
        vehicle = Vehicle(2.1, 3.1)

        self.assertEqual(2.1, vehicle.fuel)
        self.assertEqual(3.1, vehicle.horse_power)
        self.assertEqual(2.1, vehicle.capacity)
        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        # Arrange
        vehicle = Vehicle(2.1, 3.1)
        self.assertEqual(2.1, vehicle.fuel)
        self.assertEqual(1.25, vehicle.fuel_consumption)

        # Act
        vehicle.drive(1)

        # Arrange
        expected_fuel = 2.1 - (1 * 1.25)
        self.assertEqual(expected_fuel, vehicle.fuel)

    def test_drive_without_enough_fuel(self):
        vehicle = Vehicle(2.1, 3.1)
        self.assertEqual(2.1, vehicle.fuel)
        self.assertEqual(1.25, vehicle.fuel_consumption)

        with self.assertRaises(Exception) as ex:
            vehicle.drive(10)

        self.assertEqual('Not enough fuel', ex.exception.args[0])

    def test_drive_with_equal_fuel(self):
        # Arrange
        vehicle = Vehicle(2.1, 3.1)
        self.assertEqual(2.1, vehicle.fuel)
        self.assertEqual(1.25, vehicle.fuel_consumption)

        # Act
        vehicle.drive(1.68)

        # Arrange
        expected_fuel = 2.1 - (1.68 * 1.25)
        self.assertEqual(expected_fuel, vehicle.fuel)

    def test_refuel_with_enough_capacity(self):
        # Arrange
        vehicle = Vehicle(2.1, 3.1)
        self.assertEqual(2.1, vehicle.fuel)
        self.assertEqual(1.25, vehicle.fuel_consumption)

        # Act
        vehicle.refuel(0)

        # Arrange
        expected_fuel = 2.1 + 0
        self.assertEqual(expected_fuel, vehicle.capacity)

    def test_refuel_without_enough_capacity(self):
        vehicle = Vehicle(2.1, 3.1)
        self.assertEqual(2.1, vehicle.fuel)
        self.assertEqual(1.25, vehicle.fuel_consumption)

        with self.assertRaises(Exception) as ex:
            vehicle.refuel(1)

        self.assertEqual('Too much fuel', ex.exception.args[0])


    def test_string(self):
        vehicle = Vehicle(2.1, 3.1)
        result = str(vehicle)
        expected = 'The vehicle has 3.1 horse power with 2.1 fuel left and 1.25 fuel consumption'

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()