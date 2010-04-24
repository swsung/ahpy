"""Provides a simple criteria tree implementation using built-in datatypes.

The criteria and weights are stored as a simple recursive dictionary::

   {
      'id1': {'subid11': {}, 'subid21': {}},
      'id2': {'subid21': {}, 'subid22': {}},
      'id3': {}
   }

Thus a criteria element has subitems, whereas a criterion does not (empty dictionary).

"""

import sys, logging
from string import join
from fractions import Fraction
from numpy import zeros

from ahpy.core import calculateWeights


logging.basicConfig()


class AHPError(Exception):
	"An error triggered by AHP-related problem"
	

def add_criterion(criteria, parent, name):
   """Add criterion to criteria, under parent (give None as parent to add to root).

   Examples:
   
   >>> c = {}
   >>> add_criterion(c, None, "a")
   {'a': {}}
   >>> add_criterion(c, "a", "a1")
   {'a': {'a1': {}}}

   """

   if not parent:
      criteria[name] = {}

   else:
      parent = find_criterion(criteria, parent)[parent]
      parent[name] = {}

   print criteria
      

def del_criterion(criteria, name):
   """Remove a named criterion.

   Examples:

   >>> c = {"a":{"a1":{},"a2":{}},"b":{}}
   >>> del_criterion(c, "a2")
   >>> del_criterion(c, "b")
   >>> print c
   {'a': {'a1': {}}}
   """

   try:
      del find_criterion(criteria, name)[name]
      logging.info("removed %s from criteria" % name)
   except:
      raise AHPError("no '%s' criterion in criteria" % name)

      
def find_criterion(criteria, name):
   """Return the parent criteria dict.

   Examples:

   >>> c = { "a": {"a1":{}}, "b":{} }
   >>> find_criterion(c, "a")
   {'a': {'a1': {}}, 'b': {}}
   >>> find_criterion(c, "a1")
   {'a1': {}}
   >>> find_criterion(c, "b")
   {'a': {'a1': {}}, 'b': {}}

   """

   if name in criteria:
      return criteria
   else:
      for k,v in criteria.items():
         try:
            c = find_criterion(v, name)
            if c:
               return c
         except:
            pass # no subitems
            
   return None


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


