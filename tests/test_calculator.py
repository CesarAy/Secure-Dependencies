"""Tests discovered by both pytest and the standard library test runner."""

from decimal import Decimal
import unittest

from src.calculator import order_total


class OrderTotalTests(unittest.TestCase):
    def test_subtotal(self):
        self.assertEqual(order_total("12.50", 3), Decimal("37.50"))

    def test_sales_tax(self):
        self.assertEqual(order_total("10.00", 2, "0.08"), Decimal("21.60"))

    def test_rounding_to_cents(self):
        self.assertEqual(order_total("0.05", 1, "0.10"), Decimal("0.06"))

    def test_empty_order(self):
        self.assertEqual(order_total("10.00", 0), Decimal("0.00"))

    def test_invalid_inputs(self):
        for price, quantity, tax in [
            ("-1", 1, "0"), ("1", -1, "0"), ("1", 1, "-0.1"),
            ("1", 1.5, "0"), ("1", True, "0"), ("NaN", 1, "0"),
        ]:
            with self.subTest(price=price, quantity=quantity, tax=tax):
                with self.assertRaises(ValueError):
                    order_total(price, quantity, tax)
