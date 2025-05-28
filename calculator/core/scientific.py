import math

def power(base, exponent):
  """Returns base raised to the power of exponent."""
  return base ** exponent

def logarithm(x):
  """Returns the natural logarithm of x.
  Raises ValueError if x is not positive."""
  if x <= 0:
    raise ValueError("Logarithm is only defined for positive numbers")
  return math.log(x)

def logarithm10(x):
  """Returns the base-10 logarithm of x.
  Raises ValueError if x is not positive."""
  if x <= 0:
    raise ValueError("Logarithm is only defined for positive numbers")
  return math.log10(x)

def sin(x):
  """Returns the sine of x (in radians)."""
  return math.sin(x)

def cos(x):
  """Returns the cosine of x (in radians)."""
  return math.cos(x)

def tan(x):
  """Returns the tangent of x (in radians)."""
  return math.tan(x)

def asin(x):
  """Returns the arc sine of x (in radians).
  Raises ValueError if x is outside the range [-1, 1]."""
  if not -1 <= x <= 1:
    raise ValueError("Arc sine is only defined for inputs between -1 and 1")
  return math.asin(x)

def acos(x):
  """Returns the arc cosine of x (in radians).
  Raises ValueError if x is outside the range [-1, 1]."""
  if not -1 <= x <= 1:
    raise ValueError("Arc cosine is only defined for inputs between -1 and 1")
  return math.acos(x)

def atan(x):
  """Returns the arc tangent of x (in radians)."""
  return math.atan(x)
