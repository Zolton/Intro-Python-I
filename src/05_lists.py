# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print("problem 1: ", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
x.extend([8, 9, 10])
print("problem 2: ", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print("problem 3: ", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.insert(5, 99)
print("problem 4: ", x)

# Print the length of list x
# YOUR CODE HERE 

print("problem 5: lenght is ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for element in x:
    print ("problem 6: ", element*1000)
