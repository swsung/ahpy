"""
Case 1: Saaty: 'How to make a decision', p. 27.
According to Saaty, the last value rounds to 0.11. 
Todo: More tests to find out whether there's something
needing fixing or improving.

>>> from decimal import Decimal
>>> from ahpy.core import calculateWeights, calculateConsistency
>>> arr1 = [[1,3,5], [1./3., 1,3], [1./5., 1./3., 1]] 
>>> print  calculateWeights(arr1, rounding=4)
[Decimal('0.6370'), Decimal('0.2583'), Decimal('0.1047')]
>>> print calculateConsistency(arr1)
0.0213950503101

Case 2: Saaty: How to make a decision', p. 34'".

>>> arr2 = [[1    , 2    , 3    , 4    , 5],
... [1./2., 1    , 2    , 3    , 4],
... [1./3., 1./2., 1    , 2    , 3],
... [1./4., 1./3., 1./2., 1    , 2],
... [1./5., 1./4., 1./3., 1./2., 1]]
>>> print calculateWeights(arr2,rounding=3)
[Decimal('0.419'), Decimal('0.263'), Decimal('0.160'), Decimal('0.097'), Decimal('0.062')]
>>> print calculateConsistency(arr2)
0.0137258582623
"""


if __name__ == "__main__":
   import doctest
   doctest.testmod()

