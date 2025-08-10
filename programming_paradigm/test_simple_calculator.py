import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def SetUp(self):
        self.calc = SimpleCalculator()

    def TestAdd(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(2, -3), -5)

    def TestSubtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(5, 7), -2)
        self.assertEqual(self.calc.subtract(2, -3), 5)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
        self.assertEqual(self.calc.subtract(-2, 3), -5)

    def TestMultiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def TestDivide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(7, ), None)
