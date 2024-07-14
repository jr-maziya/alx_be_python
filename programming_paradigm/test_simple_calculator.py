import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2,3),5)
    def test_subtract(self):
        self.assertEqual(self.calc.add(6,3),3)
    def test_multiply(self):
        self.assertEqual(self.calc.add(2,3),6)
    def test_divide(self):
        self.assertEqual(self.calc.add(10,5),2)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()