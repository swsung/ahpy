"The test case definitions"

import sys
import unittest
from Interface.Verify import verifyClass as verify
from numarray import sum, array, shape, Float,reshape, transpose, identity, NumArray, fromlist
from LinearAlgebra2 import eigenvectors
from interfaces import *
from arraysupport import *
from utilityproviders import UtilProvider as up, RatioProviderStrategy as rps


class RA_TestCase(unittest.TestCase):
    "basic RatioArr testing"

    def testInterfaces(self):
        self.failUnless(verify(IUtilityProvider, up))
        self.failUnless(verify(IUtilityProviderStrategy, rps))

    def setUp(self):
        self.arr = RatioArr(5)

    def tearDown(self):
        del self.arr

    def testCreatedArrayIsOk(self):
        "Check that the array is empty (identity) array"

        self.assertEqual(self.arr,identity(5))


    def testEqualsBaseArray(self):
        "Create array from existing array"

        from testdata import matrices

        for m in matrices:
            r = RatioArr(basearr=m[1])
            self.assertEqual(r.shape,shape(m[1]))
            self.assertEqual(r, m[1])

    def testRatioTraversal(self):
        "Ratio pairwise permutation test using a made-up array"
        rl = []

        a= [[1.0,2.0202,3.0],[4.0,1.0,6.0],[0.07,8.0,1.0]]

        arr = RatioArr(basearr=a)

        for t in arr._traverseRatios():
            rl.append(t)

        answer= [(2.0202, 1.0, (1, 0)), (2.0202, 2.0202, (1, 1)), (2.0202, 3.0, (1, 2)), (3.0, 1.0, (2, 0)), (3.0, 2.0202, (2, 1)), (3.0, 3.0, (2, 2))]

        self.assertEqual(rl,answer)

    def testTriangleTraversal(self):
        "Ratio pairwise permutation test using a made-up array"
        rl = []

        a= [[1.0,2.0202,3.0],[4.0,1.0,6.0],[0.07,8.0,1.0]]

        arr = RatioArr(basearr=a)

        for t in arr._traverseTriangle():
            rl.append(t)

        answer= [(0, 1), (0, 2), (1, 2)]

        self.assertEqual(rl,answer)

    def testSetRatio(self):
        "Make sure ratio is written to cell and reciprocal"
        for row,col,value in [ (1,2,3.),(2,3,4.),(3,4,5.4040) ]:
            self.arr.setRatio(row,col,value)
            self.assertEqual(self.arr[row,col],float(value))
            self.assertEqual(self.arr[col,row],1./float(value))

    def testWriteDiagonal(self):
        "Make sure writing to diagonal raises error"
        self.assertRaises(RatioWriteError, self.arr.setRatio,0,0,0)

    def testOverWrite(self):
        "Make sure overwrite without force=1 raises exception"
        self.arr.setRatio(0,1,2)
        self.assertRaises(RatioWriteException, self.arr.setRatio,0,1,1)

        self.arr.setRatio(0,1,1,force=True)

    def testConsistency(self):
        "Test whether the built array is consistent"
        arr=RatioArr(5)

        for row,col,value in [ (0,1,2),(0,2,3),(0,3,4),(0,4,5) ]:
            arr.setRatio(row,col,value)
            arr.deduceRatios()

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    self.assertEqual( arr[j,k], ( arr[i,k] / arr[i,j] ) )

    def testNormalization(self):
        "Normalize array"

        barr=[[1,2,3],[4,5,6],[7,8,9]]

        arr = RatioArr(basearr=barr)
        arr._normalize()

        for c in range(len(barr)):
            self.assertEqual( sum(arr[:,c]), 1)

    def testGetRowAvgs(self):
        "Test the row average calculation"
        self.assertEqual(self.arr._getRowAvgs(),[0.2,0.2,0.2,0.2,0.2])

    def testEigen(self):
        "Get eigenvalue & vectors of the array"

        self.arr._getEigen()

    def testWeightsWithAHP(self):
        "Get weights using AHP"

        from testdata import matrices

        arr=RatioArr(basearr=matrices[0][1])

        answer = [0.63698557174475712, 0.25828499437449498, 0.10472943388074787]
        w = arr.getWeights()

        self.assertEqual(shape(w),shape(answer))
        self.assertEqual(len(w),len(answer))

        for i in range(len(answer)):
            self.assertEqual(round(w[i],5),round(answer[i],5))

    def testGetSimpleWeights(self):
        "Get weights for the array"

        from testdata import matrices

        arr=RatioArr(basearr=matrices[0][1])

        w = arr.getWeights(method='Simple')
        answer = [0.63334572030224212, 0.26049795615013005, 0.1061563235476279]

        self.assertEqual(shape(w),shape(answer))
        self.assertEqual(len(w),len(answer))

        for i in range(len(answer)):
            self.assertEqual(round(w[i],5),round(answer[i],5))

    def testGetCI(self):
        "Get CI for the array"
        self.arr.randomize()
        self.arr._getCI()


    def testGetCR(self):
        "Get CR for the array"

        from testdata import matrices

        arr=RatioArr(basearr=matrices[0][1])
        cr = matrices[0][3]

        self.assertEqual(float( str(arr.getCR())[:5] ),cr)

        arr=RatioArr(basearr=matrices[2][1])
        cr = matrices[2][3]

        self.assertEqual(float( str(arr.getCR())[:5] ),cr)

class UP_TestCase(unittest.TestCase):
    "basic utility provisioning tests"


    def setUp(self):
        self.up = up()
        self.rps = rps()
        del self.rps
    def tearDown(self):
        del self.up

    def testInstUninst(self):
        "Does strategy install and uninstall work?"
        rps_id=self.up.setStrategy(rps())
        self.up.removeStrategy(rps_id)
