from day1 import determine_fuel, determine_fuel_for_fuel
import unittest


class Day1FuelTestCase(unittest.TestCase):
    def test_day_one_12(self):
        self.assertEqual(2, determine_fuel(12))

    def test_day_one_14(self):
        self.assertEqual(2, determine_fuel(14))

    def test_day_one_1969(self):
        self.assertEqual(654, determine_fuel(1969))

    def test_day_one_100756(self):
        self.assertEqual(33583, determine_fuel(100756))


class Day1FuelForFuelTestCase(unittest.TestCase):
    def test_day_one_12(self):
        self.assertEqual(2, determine_fuel_for_fuel(12))

    def test_day_one_14(self):
        self.assertEqual(2, determine_fuel_for_fuel(14))

    def test_day_one_1969(self):
        self.assertEqual(966, determine_fuel_for_fuel(1969))

    def test_day_one_100756(self):
        self.assertEqual(50346, determine_fuel_for_fuel(100756))
