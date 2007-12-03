import decimal
from numpy import array as Array
import numpy.linalg as linalg

data = [[1,1/3.,5],[3,1,7],[0.2,1/7.,1]]

"""
data =[[1   , 2    , 3    , 4    , 5],
[1./2., 1    , 2    , 3    , 4],
[1./3., 1./2., 1    , 2    , 3],
[1./4., 1./3., 1./2., 1    , 2],
[1./5., 1./4., 1./3., 1./2., 1]]
"""

A = Array(data)

# get eigenvalues and vectors
evas, eves = linalg.eig(A)

# get primary eigenvalue and vector
prim_eva = max(evas)
prim_eva_idx = evas.tolist().index(prim_eva)
prim_eve = eves.take((prim_eva_idx,), axis=1)

# priority vector = normalized primary eigenvector
normalized = [decimal.Decimal(str(abs(v[0])))._round(3) for v in (prim_eve / sum(prim_eve))]
print normalized