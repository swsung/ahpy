from decimal import Decimal
from ahpy.core import calculateWeights, calculateConsistency

# Saaty: 'How to make a decision', p. 27
# SAccording to Saaty, the last value rounds to 0.11. 
# Todo: More tests to find out whether there's something
# needing fixing or improving.

arr1 = [[1,3,5], [1./3., 1,3], [1./5., 1./3., 1]] 
w1 = calculateWeights(arr1, rounding=4)
try:
   assert(w1==[Decimal('0.6370'), Decimal('0.2583'), Decimal('0.1047')])
except:
   print w1
   
print calculateConsistency(arr1)
# 0.037

# Saaty: How to make a decision', p. 34'",

arr2 = [
[1    , 2    , 3    , 4    , 5],
[1./2., 1    , 2    , 3    , 4],
[1./3., 1./2., 1    , 2    , 3],
[1./4., 1./3., 1./2., 1    , 2],
[1./5., 1./4., 1./3., 1./2., 1]]

w2 = calculateWeights(arr2,rounding=3)

try:
   assert(w2 == [Decimal('0.419'), Decimal('0.263'), Decimal('0.160'), Decimal('0.097'), Decimal('0.062')])
except AssertionError:
   print w2

print calculateConsistency(arr2)
   
# 0.015