"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

#f = open("foo", "r")
# with open("src/foo.txt") as f:
#     read_data = f.read()

# print(f.read())

def read_only(x):
    file1 = open(x, "r")
    readFile = file1.read()
    file1.close()
    return readFile
print(read_only("src/foo.txt"))







# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

def read_write(x):
    file1 = open("bar.txt", "a")
    file1.write(x)
    file1.close()

bar_text = input("Write your novel: ")
read_write(bar_text)
print("Your novel, sir: ", read_only("bar.txt"))

# YOUR CODE HERE