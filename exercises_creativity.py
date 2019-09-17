"""Creativity exercies. - Chapter 1."""

#C-1.13: Write a pseudo-code description of a function that reverses a list of 
#n intergers, so that the numbers are listed in the opposite order than they were before, and
#compare this method to an equivalent python function for doing the same thing.

"""The equivalent python function is the sort method. (in reverse)"""
def revlist(mylist):
	revdlist = [] #a new list to store reversed elements.
	for i in range(1,len(mylist)+1):
		revdlist.append(mylist[-i])
	print(revdlist)
mylist = [1,2,3,4,5]
revlist(mylist)		


