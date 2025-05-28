import unittest
import math
from calculator.core.scientific import power, logarithm, logarithm10, sin, cos, tan, asin, acos, atan

class TestScientificFunctions(unittest.TestCase):

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(2, -2), 0.25)
        self.assertAlmostEqual(power(4, 0.5), 2.0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(math.e), 1)
        self.assertAlmostEqual(logarithm(1), 0)
        self.assertAlmostEqual(logarithm(math.exp(5)), 5)

    def test_logarithm_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            logarithm(0)
        self.assertEqual(str(context.exception), "Logarithm is only defined for positive numbers")
        with self.assertRaises(ValueError):
            logarithm(-1)

    def test_logarithm10(self):
        self.assertAlmostEqual(logarithm10(10), 1)
        self.assertAlmostEqual(logarithm10(100), 2)
        self.assertAlmostEqual(logarithm10(1), 0)
        self.assertAlmostEqual(logarithm10(0.1), -1)

    def test_logarithm10_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            logarithm10(0)
        self.assertEqual(str(context.exception), "Logarithm is only defined for positive numbers")
        with self.assertRaises(ValueError):
            logarithm10(-10)

    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(math.pi / 2), 1)
        self.assertAlmostEqual(sin(math.pi), 0, places=6) # Higher precision for pi
        self.assertAlmostEqual(sin(3 * math.pi / 2), -1)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(math.pi / 2), 0, places=6) # Higher precision
        self.assertAlmostEqual(cos(math.pi), -1)
        self.assertAlmostEqual(cos(3 * math.pi / 2), 0, places=6) # Higher precision

    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(math.pi / 4), 1)
        # tan(pi/2) is undefined (approaches infinity), so we test values close to it if needed
        # or avoid such direct tests. For now, testing known values.

    def test_asin(self):
        self.assertAlmostEqual(asin(0), 0)
        self.assertAlmostEqual(asin(1), math.pi / 2)
        self.assertAlmostEqual(asin(-1), -math.pi / 2)
        self.assertAlmostEqual(asin(0.5), math.pi / 6)

    def test_asin_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            asin(1.1)
        self.assertEqual(str(context.exception), "Arc sine is only defined for inputs between -1 and 1")
        with self.assertRaises(ValueError):
            asin(-1.1)

    def test_acos(self):
        self.assertAlmostEqual(acos(1), 0)
        self.assertAlmostEqual(acos(0), math.pi / 2)
        self.assertAlmostEqual(acos(-1), math.pi)
        self.assertAlmostEqual(acos(0.5), math.pi / 3)

    def test_acos_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            acos(1.1)
        self.assertEqual(str(context.exception), "Arc cosine is only defined for inputs between -1 and 1")
        with self.assertRaises(ValueError):
            acos(-1.1)

    def test_atan(self):
        self.assertAlmostEqual(atan(0), 0)
        self.assertAlmostEqual(atan(1), math.pi / 4)
        self.assertAlmostEqual(atan(-1), -math.pi / 4)
        # atan approaches pi/2 as input goes to infinity, -pi/2 for -infinity

if __name__ == '__main__':
    unittest.main()
