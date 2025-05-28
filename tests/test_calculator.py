import unittest
import math
from calculator.core.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_initial_state(self):
        self.assertEqual(self.calc.get_current_value(), 0.0)
        self.assertEqual(self.calc.memory_value, 0.0)

    def test_set_current_value_directly(self):
        self.calc.current_value = 5.0
        self.assertEqual(self.calc.get_current_value(), 5.0)

    def test_add(self):
        self.calc.add(5)
        self.assertEqual(self.calc.get_current_value(), 5.0)
        self.calc.add(3)
        self.assertEqual(self.calc.get_current_value(), 8.0)
        self.calc.add(-2)
        self.assertEqual(self.calc.get_current_value(), 6.0)

    def test_subtract(self):
        self.calc.current_value = 10.0
        self.calc.subtract(3)
        self.assertEqual(self.calc.get_current_value(), 7.0)
        self.calc.subtract(7)
        self.assertEqual(self.calc.get_current_value(), 0.0)
        self.calc.subtract(-5)
        self.assertEqual(self.calc.get_current_value(), 5.0)

    def test_multiply(self):
        self.calc.current_value = 2.0
        self.calc.multiply(3)
        self.assertEqual(self.calc.get_current_value(), 6.0)
        self.calc.multiply(0)
        self.assertEqual(self.calc.get_current_value(), 0.0)
        self.calc.current_value = 5.0
        self.calc.multiply(-2)
        self.assertEqual(self.calc.get_current_value(), -10.0)

    def test_divide(self):
        self.calc.current_value = 6.0
        self.calc.divide(3)
        self.assertEqual(self.calc.get_current_value(), 2.0)
        self.calc.divide(0.5)
        self.assertEqual(self.calc.get_current_value(), 4.0)

    def test_divide_by_zero(self):
        self.calc.current_value = 5.0
        with self.assertRaises(ValueError) as context:
            self.calc.divide(0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
        self.assertEqual(self.calc.get_current_value(), 5.0) # Value should not change

    def test_power(self):
        self.calc.current_value = 2.0
        self.calc.power(3)
        self.assertEqual(self.calc.get_current_value(), 8.0)
        self.calc.current_value = 9.0
        self.calc.power(0.5)
        self.assertEqual(self.calc.get_current_value(), 3.0)

    def test_log(self):
        self.calc.current_value = math.e
        self.calc.log()
        self.assertAlmostEqual(self.calc.get_current_value(), 1.0)

    def test_log_invalid(self):
        self.calc.current_value = 0
        with self.assertRaises(ValueError):
            self.calc.log()
        self.calc.current_value = -1
        with self.assertRaises(ValueError):
            self.calc.log()

    def test_log10(self):
        self.calc.current_value = 100.0
        self.calc.log10()
        self.assertAlmostEqual(self.calc.get_current_value(), 2.0)

    def test_log10_invalid(self):
        self.calc.current_value = 0
        with self.assertRaises(ValueError):
            self.calc.log10()
        self.calc.current_value = -10
        with self.assertRaises(ValueError):
            self.calc.log10()
            
    def test_sin(self):
        self.calc.current_value = math.pi / 2
        self.calc.sin()
        self.assertAlmostEqual(self.calc.get_current_value(), 1.0)

    def test_cos(self):
        self.calc.current_value = math.pi
        self.calc.cos()
        self.assertAlmostEqual(self.calc.get_current_value(), -1.0)

    def test_tan(self):
        self.calc.current_value = math.pi / 4
        self.calc.tan()
        self.assertAlmostEqual(self.calc.get_current_value(), 1.0)

    def test_asin(self):
        self.calc.current_value = 1.0
        self.calc.asin()
        self.assertAlmostEqual(self.calc.get_current_value(), math.pi / 2)

    def test_asin_invalid(self):
        self.calc.current_value = 1.1
        with self.assertRaises(ValueError):
            self.calc.asin()
        self.calc.current_value = -2
        with self.assertRaises(ValueError):
            self.calc.asin()

    def test_acos(self):
        self.calc.current_value = 0.0
        self.calc.acos()
        self.assertAlmostEqual(self.calc.get_current_value(), math.pi / 2)

    def test_acos_invalid(self):
        self.calc.current_value = 1.5
        with self.assertRaises(ValueError):
            self.calc.acos()
        self.calc.current_value = -1.1
        with self.assertRaises(ValueError):
            self.calc.acos()

    def test_atan(self):
        self.calc.current_value = 1.0
        self.calc.atan()
        self.assertAlmostEqual(self.calc.get_current_value(), math.pi / 4)

    def test_clear(self):
        self.calc.current_value = 10.0
        self.calc.clear()
        self.assertEqual(self.calc.get_current_value(), 0.0)

    def test_memory_store_recall(self):
        self.calc.current_value = 42.0
        self.calc.memory_store()
        self.assertEqual(self.calc.memory_value, 42.0)
        self.calc.current_value = 10.0 # Change current value
        self.calc.memory_recall()
        self.assertEqual(self.calc.get_current_value(), 42.0)

    def test_memory_clear(self):
        self.calc.current_value = 123.0
        self.calc.memory_store()
        self.assertEqual(self.calc.memory_value, 123.0)
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory_value, 0.0)
        # Recalling after clear should set current value to 0 (memory_value)
        self.calc.current_value = 5.0 
        self.calc.memory_recall()
        self.assertEqual(self.calc.get_current_value(), 0.0)

    def test_chained_operations(self):
        self.calc.add(10)      # current = 10
        self.calc.subtract(3)  # current = 7
        self.calc.multiply(2)  # current = 14
        self.calc.divide(7)    # current = 2
        self.calc.power(3)     # current = 8
        self.assertEqual(self.calc.get_current_value(), 8.0)

    def test_operations_with_memory(self):
        self.calc.add(5)           # current = 5
        self.calc.memory_store()   # memory = 5
        self.calc.add(10)          # current = 15
        self.calc.subtract(self.calc.memory_value) # current = 15 - 5 = 10
        self.assertEqual(self.calc.get_current_value(), 10.0)
        self.calc.memory_recall()  # current = 5
        self.assertEqual(self.calc.get_current_value(), 5.0)

if __name__ == '__main__':
    unittest.main()
