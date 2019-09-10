#Reinforcement exercise solutions.


################################################################
#R-1.1 (A function, is_mutliple(n,m), that takes two integer
# values and returns True if n is a multiple of m, n=mi for some integer i
# and returns False otherwise.
def is_multiple(n,m):
	output = True if n % m == 0 else False
	print(output)
	
#is_multiple(15,5)

############################################################
#R-1.2 (A function, is_even(k), that takes an integer value and 
# returns True if k is even and False otherwise. However, function cannot
# use the multiplication,modulo or divison operators.
def is_even(k):
	g= str(k)
	output = True if g[-1] in "02468"  else False
	print(output)
#is_even(38)

#################################################################
#R-1.3 (A function minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in a form of a tuple of length two.
# Not using the built-in function min/max in solution

def minmax(data):
	min_data = 0 #set minimum to zero
	max_data = 0 #set maximum to zero
	temp = data[0] #temp value to aid iteration.
	final = []
	for i in data:
		if i <= temp:
			min_data = i #find min
		elif i >= temp:
			 max_data = i #find max
	final.append(min_data)
	final.append(max_data)
	output = tuple(final)
	print(output)	   
	
#minmax([2,4,7,1,21,0])
	
###################################################################
#R-1.4 (A function that takes a positive integer n and returns the sum
# of the squares of all positive integers small than n.
def return_sum_squares(n):
	output =list((k*k for k in range(1, n)))
	final_sum = 0
	for i in output:
		final_sum = final_sum + i
	print(final_sum)
	
#return_sum_squares(5)
	

####################################################################
#R-1.5 (A command that computes the sum from R-1.4), using built-in function.
def return_sum_squares1(p):
	output = sum(k*k for k in range(1,p))
	print(output)
	
#return_sum_squares1(5)

############################################################################
#R-1.6 A function that takes a positive integer n and returns the sum of the 
# squares of all the odd positive integers smaller than n
def sum_squares_odd(n):
	output = []
	for k in range(1,n):
		if k %2 != 0:
			output.append(k*k)
	print(output)
	
#sum_squares_odd(5)



#R-1.7 A function that takes a positive integer n and returns the sum of the 
# squares of all the odd positive integers smaller than n
def sum_squares_odd(n):
	output = list(k*k for k in range(1,n) if k%2 !=0)
	print(output)
	
#sum_squares_odd(5)

#R-1.8 Python allows negative integers to be used as indices into a sequence
# such as a string. If a string s has length n, and expression s[k] is used
# for index -n<= k < 0, what is the equivalent index j>=0 such that s[j] 
# references the same element?
def return_element(data,k):
	"""Tells you the equivalent negative index."""
	eq_neg_index = k - len(data)
	print(data[eq_neg_index], eq_neg_index if data else False)
	

l = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1] 
return_element(l,0)


#R-1.9 What parameters should be sent to the range constructor, to produce
# a range with values 50,60,70,80?
def try_range():
	output = list(range(50,90,10))
	print(output)
	
#try_range()
		
#R-1.10 What parameter should be sent to the range constructor, to produce a range with values 8,6,4,2,0,-2,-6,-8
def neg_range():
	print(list(range(8,-10, -2)))
	
#neg_range()	

#R-1.11 Demonstrate how to use python's list comprehensions syntax to produce the list
# [1,2,4,8,16,32,64,128,258]

def two_n(n):
	output = [ 2**n for n in range(0,n)]
	print(output)
	
#two_n(8)

#R-1.12 Python's random module includes a function choice(data) that returns a random element
# from a non-empty sequence. Using only the randrange function, implement your own version of the 
# choice function.













