import unittest
from main import calculate_total


class TestCalculateTotal(unittest.TestCase):

    def test_gst_calculation(self):
        self.assertEqual(calculate_total(100), 105.00)

    def test_zero_amount(self):
        self.assertEqual(calculate_total(0), 0.00)

    def test_decimal_amount(self):
        self.assertEqual(calculate_total(200), 210.00)


if __name__ == "__main__":
    unittest.main()
