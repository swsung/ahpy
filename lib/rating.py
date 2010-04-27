"""
Module that provides various utilities to support AHP pairwise comparisons,
or ratings, of criteria and alternatives.

Comparisons are stored in lists of (alternative1, alternative2, value) tuples.
   
Each tuple is thus a comparison between the first alternative to the second,
using a scale from 1 to 9. Value 1 means the alternatives are equally
preferable,and 9 means the first alternative is absolutely more preferred
to the second one.

"""

from fractions import Fraction
from numpy import zeros


def generate_array(comparisons):
   """Parse ratings, return list of alternatives & pairwise comparisons array.
      
   The set of ratings is expeted to be complete - all alternatives must be
   rated against one another. Example:
   
   >>> comparisons = [("apple", "orange", 5),
   ... ("apple", "banana", 4), ("orange", "banana",1)]
   >>> results = generate_array(comparisons)
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
   arr = zeros((size, size))
   for i in range(size):
      arr[i, i] = 1


   # Fill in the comparison data, including reciprocal values  
   for a1, a2, r in comparisons:
      y = alternatives.index(a1)
      x = alternatives.index(a2)
      arr[y, x] = r
      if not arr[x, y]:
         arr[x, y] = Fraction("1/%i" % r)
         
   return (alternatives, arr)
   
   
   
if __name__ == "__main__":
   import doctest
   doctest.testmod()


