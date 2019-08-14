#A generator is implemented with a syntax that is very similar 
# to a function but instead of returning values, a 'yield' statement 
# is executred to indicate each element of the series.

# This code implements a generator for computing factors of a number.

def factors(n):   #generator that computes factors
	for k in range(1, n+1):
		if n % k == 0: #divides evenly, thus k is a factor
			yield k #yield this factor as next result.

#creating an instance of our generator.			
#for factor in factors(100):
#	print factor

#Example 2, still on generators to compute factors.
# This time by only testing values up to the square root of that number.

def factorss(n):
	k = 1
	while k * k < n:  # while k < sqrt(n)
		if n % k == 0:
			yield k
			yield n // k
		k += 1
	if k * k == n: #special case if n is perfect square
		yield k
		
for factor in factorss(5):
	print factor
			
