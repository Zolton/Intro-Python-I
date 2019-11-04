"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
import math
x = 10
y = 2.24552
z = "I like turtles!"

def round_up (n, decimals = 0):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier) / multiplier

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print("first time: x is %s, y is %s, z is %s" % (x, round_up(y, 2), z))



# Use the 'format' string method to print the same thing

print("second timex is {2}, y is {1}, z is {0}".format(z, round_up(y, 2), x))


# Finally, print the same thing using an f-string

print(f"third time: x is {x}, y is {round_up(y, 2)}, z is {z}")