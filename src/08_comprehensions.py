"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [gabba + 1 for gabba in range(5)]
# for gabba in range(5):
#     y.append(gabba + 1)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]



y = [gabba**3 for gabba in range(10)]
# for gabba in range(10):
#     y.append(gabba**3)

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [gabba.upper() for gabba in a]
# for gabba in a:
#     y.append(gabba.upper())

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
evens = [i for i in x if int(i) % 2 == 0]

# if gabba in x % 2 == 0:
#     y.append(gabba)

print(evens)