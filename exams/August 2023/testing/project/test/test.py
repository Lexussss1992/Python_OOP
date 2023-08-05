from unittest import TestCase

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.second_hand_car = SecondHandCar('Fiat', 'X', 200, 1000)

    def test_valid_init(self):
        self.assertEqual('Fiat', self.second_hand_car.model)
        self.assertEqual('X', self.second_hand_car.car_type)
        self.assertEqual(200, self.second_hand_car.mileage)
        self.assertEqual(1000, self.second_hand_car.price)
        self.assertEqual([], self.second_hand_car.repairs)

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as ve:
            SecondHandCar('Fiat', 'X', 200, 1.0)
        self.assertEqual(str(ve.exception),'Price should be greater than 1.0!')

    def test_invalid_mileage(self):
        with self.assertRaises(ValueError) as ve:
            SecondHandCar('Fiat', 'X', 100, 2.0)
        self.assertEqual(str(ve.exception),'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price_new_price_greater_than_self__price(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(3000.0)
        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')

    def test_set_promotional_price_new_price_less_than_self_price(self):
        res = self.second_hand_car.set_promotional_price(100.0)

        self.assertEqual('The promotional price has been successfully set.', res)

    def test_need_repair_repair_price_greater_than_self(self):
        res = self.second_hand_car.need_repair(1000, 'alabala')

        self.assertEqual('Repair is impossible!', res)

    def test_need_repair_valid(self):
        res = self.second_hand_car.need_repair(100, 'alabala')

        self.assertEqual(1100, self.second_hand_car.price)
        self.assertEqual(['alabala'], self.second_hand_car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', res)

    def test_gt(self):
        res = self.second_hand_car.__gt__(SecondHandCar('Skoda', 'Y', 200, 2000))

        self.assertEqual('Cars cannot be compared. Type mismatch!', res)

    def test_gt_valid(self):
        res = self.second_hand_car.__gt__(SecondHandCar('Skoda', 'X', 200, 500))

        self.assertEqual(True, res)

    def test_str(self):
        res = self.second_hand_car.__str__()
        res_text = "Model Fiat | Type X | Milage 200km\nCurrent price: 1000.00 | Number of Repairs: 0"

        self.assertEqual(res_text, res)
