import unittest
from random import random, randint

from calculations import calculations
from utils import exceptions


class TestRepayments(unittest.TestCase):

    def test_monthly_repayment_with_negative_value_raises_exception(self):
        salary = -5
        self.assertRaises(
            exceptions.LessThanZeroException,
            calculations.calculate_monthly_repayment,
            salary
        )

    def test_monthly_repayment_returns_zero_if_below_threshold(self):
        min_input_value = 0
        max_input_value = calculations.REPAYMENT_THRESHOLD
        for i in range(0, 3):
            value = random()
            scaled_value = min_input_value + (
                value * (calculations.REPAYMENT_THRESHOLD - min_input_value)
            )
            with self.subTest(input_salary=scaled_value):
                self.assertEqual(
                    calculations.calculate_monthly_repayment(scaled_value),
                    0.00
                )

    def test_monthly_repayment_returns_valid_calculation(self):
        value = calculations.REPAYMENT_THRESHOLD + 1200
        self.assertEqual(
            calculations.calculate_monthly_repayment(value),
            100 * calculations.REPAYMENT_RATE
        )
