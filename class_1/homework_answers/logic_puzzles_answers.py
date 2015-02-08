# ANSWER 1:
# x = 5

# Example trace through code
def f(x):         # x = 5
  z = x           # z = 5 =>
  z *= 3          # z = 15 =>
  z -= 10         # z = 5 =>
  z **= 2         # z = 25 =>
  z -= x          # z = 20
  print z == 20   # 20 == 20


# Answer 2:
# x = string with odd length, y equals an integer equal to 30 / len(x)
# Example solutions:
# 1. x = "yes", y = 10
# 2. x = "string", y = 6

# Example trace through code
def g(x, y):          # x = 'yes', y = 10
  z = len(x)          # z = 3
  a = z % 2           # a = 1
  a *= y              # a = 10
  b = x * a           # b = 'yesyesyesyesyesyesyesyesyesyes'
  print len(b) == 30  # 30 == 30


# Answer 3:
# x and y can be any value (True or False), z = 8 or -6

# Example trace through code
def h(x, y, z):       # x = True, y = True, z = 8
    a = x and not y   # a = False
    b = a * z         # b = 0
    z -= 1            # z = 7
    z **= 2           # z = 49
    print z == 49     # 49 = 49


# Answer 4:
def is_odd(x):
    print x % 2 == 1

# Answer 5
def is_divisible(x, y):
    print x % y == 0

# Answer 6
# The idea behind this answer is that for a triangle to be a right triangle, the Pythagorean Theorem must hold for its sides
# (a^2 + b^2) = c^2
# Since we do not know what side is the hypotenuse (longest side) we have to check check if the formula holds when any of
# the sides are the hypotenuse
def is_right_triangle(a, b, c):
    a_hypotenuse = a**2 == b**2 + c**2
    b_hypotenuse = b**2 == c**2 + c**2
    c_hypotenuse = c**2 == a**2 + b**2
    print a_hypotenuse or b_hypotenuse or c_hypotenuse
