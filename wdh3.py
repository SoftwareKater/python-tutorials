
def myfunc(x, y):
	z = 2*x + y
	return z

# Consider lines 2-4:
# a) What happens in those lines? A function is defined.
	# z is given from a formular
# b) What is the name of the function?
	# myfunc
# c) How many arguments does it take?
	# 2
# d) In more detail: is it a deamon (no input and no output), is it a process (no output) or is it a function (has both input and output)?
	# 
# e) Call the function on the following values: (x=5, y=3), (x=[1, 2, 3], y=[9, 8, 7]) and (x=(1, 2, 3), y=(9, 8, 7))?



# f) There are more data types in python! Which types lead to an error, if plugged into myfunc?
# g) What is the console output of line 19? (Uncomment to check)

res = myfunc(myfunc(-3, 1), 7-1) - 1
#print(res)

# h) What is the console output of line 24?

res_1 = myfunc("", "Joha") + myfunc("n", "es")
print(res_1)

# We know functions since the first contanct with python:
# print(some_string) -> prints out the string to console
# len(some_iterable) -> takes a sequence (e.g. list, tuple) and returns the length of the sequence
# list(some_iterable) -> creates a list from the given iterable
# analogously set, tuple, ...
# int(some_number) -> takes a number, and tries to convert it to an integer
# analogously float, str, bool, ...
# Those are called build-in functions, and knowing some of them speeds up developing process!
# Go to the official python documentation and read about build in functions. Pick at least three of them 
# and use the following space, to play around with them. Call them on various inputs, print out the outputs, 
# maybe try to combine them, ...



# The next two assignments ask you to construct functions on your own. You get some piece of code that 
# implements some functionality, and you have to construct a function that has the same functionality.
# The following for-loop...

T = 8
for i in range(T):
	print(i)

# depends on the parameter T but does not calculate anything (it just prints to console). Define a function 
# "print_numbers_upto", which takes a number and prints out all numbers starting from zero up to the given number. 



# The following while-loop:

while True:
	p = input("Please give an integer: ")
	try:
		p = int(p)
		break
	except ValueError:
		pass

# Asks for input, until it gets an input, which is convertible to an integer (p = int(p)). It does not depend on 
# any parameter, but it "calculates" the value p. Define a function "get_input", which implements exactly this 
# while-loop. It takes no parameters and returns the choice p.



# Go back to one of the games that you have coded. Copy the code into a new file and do the follwoing steps:
# 1) Break the code into logically connected (sub-)sections. Mark them with comments.
# 2) Each of those sections will depend on certain parameters, e.g. the number of the current round, 
#	 the number of the player whose turn it is, decisions that have been made by players, etc. 
#	 Include this information in the comments marking the sections
# 3) Some of the sections will calculate intermediate values, that are needed by other sections further 
#	 down in the code. If a section calculates intermediate results, include this in the marking comment.
# 4) For each section, write a function, that implements exactly the functionality of the section. Use 
# 	 the comments to decide whether and how many arguments a function must have and to decide, whether 
# 	 the function needs a return value.
# 5) Write a function "gameloop()". It does not take any arguments. In the body of this function you should call 
#	 all the functions that you defined in 4) (in the right order and with the correct arguments).
