from . import operations
from . import scientific

class Calculator:
    def __init__(self):
        self.current_value = 0.0
        self.memory_value = 0.0

    def add(self, x):
        self.current_value = operations.add(self.current_value, x)
        return self.current_value

    def subtract(self, x):
        self.current_value = operations.subtract(self.current_value, x)
        return self.current_value

    def multiply(self, x):
        self.current_value = operations.multiply(self.current_value, x)
        return self.current_value

    def divide(self, x):
        self.current_value = operations.divide(self.current_value, x)
        return self.current_value

    def power(self, exponent):
        self.current_value = scientific.power(self.current_value, exponent)
        return self.current_value

    def log(self):
        self.current_value = scientific.logarithm(self.current_value)
        return self.current_value

    def log10(self):
        self.current_value = scientific.logarithm10(self.current_value)
        return self.current_value

    def sin(self):
        self.current_value = scientific.sin(self.current_value)
        return self.current_value

    def cos(self):
        self.current_value = scientific.cos(self.current_value)
        return self.current_value

    def tan(self):
        self.current_value = scientific.tan(self.current_value)
        return self.current_value

    def asin(self):
        self.current_value = scientific.asin(self.current_value)
        return self.current_value

    def acos(self):
        self.current_value = scientific.acos(self.current_value)
        return self.current_value

    def atan(self):
        self.current_value = scientific.atan(self.current_value)
        return self.current_value

    def clear(self):
        self.current_value = 0.0
        return self.current_value

    def memory_store(self):
        self.memory_value = self.current_value

    def memory_recall(self):
        self.current_value = self.memory_value
        return self.current_value

    def memory_clear(self):
        self.memory_value = 0.0

    def get_current_value(self):
        return self.current_value
