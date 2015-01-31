# Reasoning Over Code
# For each of the following functions: f, g, h find the value of the arguments that will make the function print true

def f(x):
  z = x
  z *= 3
  z -= 10
  z **= 2
  z -= x
  print z == 20

def g(x, y):
  z = len(x)
  a = z % 2
  a *= y
  b = x * a
  print len(b) == 30


def h(x, y, z):
    a = x and not y
    b = a * z
    z -= 1
    z **= 2
    print z == 49


# Complete the logic in the functions
# Function 1: is_odd(x)
# Prints True if x is odd and false if it is even
def is_odd(x):
    print x

# Function 2: is_divisible(x, y)
# Prints True if x and y are both integer types and x is divisible by y, and False otherwise
def is_divisible(x, y):
    print x, y

# Function 3: is_right_triangle(a, b, c)
# Prints True if the three values passed in could be the sides of a right triangle
# Hint: use the Pythagorean Theorem
def is_right_trinangle(a, b, c):
    print a, b, c
