"""
Module for various utilities related to using AHP.
"""

def comparisons2array(comparisons):
	"""Parse ratings, return list of alternatives and a pairwise comparisons array.
	
	Comparisons are expected as a list of (alternative1, alternative2, value) tuples.
	
	They compare the first alternative to the second using a scale from 1 to 9, where
	value 1 means the alternatives are equally preferable, and 9 means the first
	alternative is absolutely more preferred to the second.
   
	The set of ratings is expeted to be complete - all alternatives must be
	rated against one another.
	
	Example:

	We by and large prefer apples to oranges as well as to bananas. Thus:
	
	>>> comparisons = [("apple", "orange", 5), ("apple", "banana", 4), ("orange", "banana",1)]
	>>> results = comparisons2array(comparisons)
	>>> results[0]
	['apple', 'orange', 'banana']
	>>> results[1]
   	array([[ 1.  ,  5.  ,  4.  ],
   	       [ 0.2 ,  1.  ,  1.  ],
   	       [ 0.25,  1.  ,  1.  ]])
	"""

	# First, determine the set of alternatives
	alternatives = []
	for a1, a2, r in comparisons:
		if a1 not in alternatives:
			alternatives.append(a1)
		if a2 not in alternatives:
			alternatives.append(a2)
	
	# Create a identity matrix to start from
	size = len(alternatives)	
	arr = zeros((size,size))
	for i in range(size):
		arr[i,i] = 1


	# Fill in the comparison data, including reciprocal values	
	for a1, a2, r in comparisons:
		y = alternatives.index(a1)
		x = alternatives.index(a2)
		arr[y,x] = r
		if not arr[x,y]:
			arr[x,y] = Fraction("1/%i" % r)
			
	return (alternatives, arr)
	
	
	
if __name__ == "__main__":
   import doctest
   doctest.testmod()


