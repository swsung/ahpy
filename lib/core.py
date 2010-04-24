"This module provides support for calculating AHP weights and consistency ratios (CR)"

from decimal import Decimal as D
from fractions import Fraction as F
from numpy import array, diagonal
from numpy.linalg import eig


# Random index devised by Saaty. Used for Consistency Ratio (CR) calculation.

RI = (0, 0, D('0.58'), D('0.9'), D('1.12'),
      D('1.24'), D('1.32'), D('1.41'), D('1.45'), D('1.49'),
      D('1.51'), D('1.48'), D('1.56'), D('1.57'), D('1.59')
)


def calculateWeights(arr, rounding=4):
   """Given pairwise comparisons array, calculate weights using the AHP method.

   Take the following example array:

   +-----+-----+---+
   |  1  | 1/3 | 5 |
   +-----+-----+---+
   |  3  |  1  | 7 |
   +-----+-----+---+
   | 1/5 | 1/7 | 1 |
   +-----+-----+---+

   Set up the array:

   >>> arr = array([ [1, 1./3, 5], [3,1,7], [1./5,1./7,1] ])

   Calculate the weights (= normalized primary eigenvector):

   >>> calculateWeights(arr, rounding=4)
   [Decimal('0.2790'), Decimal('0.6491'), Decimal('0.0719')]
   """

   PLACES = D(10) ** -(rounding)
   
   # get eigenvalues and vectors
   evas, eves = eig(arr)

   # get primary eigenvalue and vector
   eva = max(evas)
   eva_idx = evas.tolist().index(eva)
   eve = eves.take((eva_idx,), axis=1)

   # priority vector = normalized primary eigenvector
   normalized = eve / sum(eve)

   # turn into list of real part values
   vector = [abs(e[0]) for e in normalized]

   # return nice rounded Decimal values
   return [ D( str(v) ).quantize(PLACES) for v in vector ]


def calculateConsistency(arr):
   """Given pairwise comparisons array, calculate consistency ratio (CR) for the comparisons.
   
   Example:
   
   >>> arr = array([ [1, 1./3, 1./9, 1./5], [3,1,1,1], [9,1,1,3], [5,1,1./3,1] ])
   >>> print calculateConsistency(arr)
   0.0557579272574
   
   """
   
   # get largest (ie. primary) eigenvalue
   eva = max(eig(arr)[0]).real
   
   # calculate consistency index (CI)
   n = len(arr)
   CI = (eva-n) / (n-1)
   
   # return CR
   return CI / float(RI[n])
	

if __name__ == "__main__":
    import doctest
    doctest.testmod()
