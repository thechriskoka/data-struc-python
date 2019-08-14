#Reinforcement exercise solutions.


################################################################
#R-1.1 (A function, is_mutliple(n,m), that takes two integer
# values and returns True if n is a multiple of m, n=mi for some integer i
# and returns False otherwise.
def is_multiple(n,m):
	output = True if n % m == 0 else False
	print output
	
#is_multiple(15,5)

############################################################
#R-1.2 (A function, is_even(k), that takes an integer value and 
# returns True if k is even and False otherwise. However, function cannot
# use the multiplication,modulo or divison operators.
def is_even(k):
	g= str(k)
	output = True if g[-1] in "02468"  else False
	print output 
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
	print output		   
	
#minmax([2,4,7,1,21,0])
	
###################################################################
#R-1.4 (A function that takes a positive integer n and returns the sum
# of the squares of all positive integers small than n.
def return_sum_squares(n):
	output =list((k*k for k in range(1, n)))
	final_sum = 0
	for i in output:
		final_sum = final_sum + i
	print final_sum
	
#return_sum_squares(5)
	

####################################################################
#R-1.5 




















