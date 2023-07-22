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

    def test_string(self):
        vehicle = Vehicle(2.1, 3.1)

        self.assertEqual('The vehicle has 3.1 horse power with 2.1 fuel left and 1.25 fuel consumption', vehicle.__str__())


if __name__ == '__main__':
    unittest.main()