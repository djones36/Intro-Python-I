"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

# foo_file = open('foo.txt')
# print((foo_file.read()))

# print(foo_file.close())
with open('foo.txt') as f:
    read_data = f.read()
    print(read_data)
    f.close()
    print("foo.txt is closed: ", f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar_file =open('bar.txt', 'w')
bar_file.write("three\nnew\nlines")
bar_file.close()
print('bar.txt is close ', bar_file.closed)