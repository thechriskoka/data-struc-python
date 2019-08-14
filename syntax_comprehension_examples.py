#Demonstrating the use of comprehension syntax
# [ expression for value in iterable if condition ]

def squares(n):
	squares = [k*k for k in range(1, n+1)]
	print squares
	
def factors(g):
	factors = [k for k in range(1,g+1) if g % k == 0]
	print factors
	
#Compute sum of first n squares
def square_sum(n):
	total = sum(k*k for k in range(1, n+1))
	print total 

squares(10)	
square_sum(10)
