"Ratio array support for AHP"

from random import randrange
import sys
from numpy import sum, array, shape, Float,reshape, transpose, identity, NumArray, fromlist
from LinearAlgebra2 import eigenvectors

class RatioArr(NumArray):
	"AHP support"	
	def __init__(self,s=5, basearr=None):
			
		if basearr is None:
			buf=identity(s,Float)._data
									
		elif type(basearr) == list:
			s=len(basearr)
			sh=shape(basearr)
			if len(sh)==2 and s==sh[1]:
				buf=fromlist(basearr,type=Float,shape=(s,s))._data
			else:
				raise TypeError, "invalid base array shape: %s" % sh
		else:
			raise TypeError, "invalid base array type: %s" % type(basearr)

		NumArray.__init__(self,(s,s),Float,buffer=buf)
		
	def randomize(self):
		for r,c in self._traverseTriangle():
			self.setRatio(r,c,randrange(1,10),force=True)
			
	def setRatio(self,r,c,ratio,force=False):
		"Assign a ratio value to cell"
		
		ratio = float(ratio)
		
		"Writing to diagonal is not allowed"
		if r == c:
			raise RatioWriteError((r,c))		
		
		"If force is not set, write if target is empty"
		if not force:
			if self[r,c] == 0:
				self[r,c] = ratio
				self[c,r] = 1/ratio
			else:
				raise RatioWriteException((r,c), self[r,c])
		
		"Write if 'force' is set" 
		if force:
			self[r,c] = ratio
			self[c,r] = 1/ratio
			
	def deduceRatios(self,row=0,force=0):
		locs=[]
		for elm1,elm2,loc in self._traverseRatios(row=row):		
			if self[loc] == 0: # if target cell is empty
					if elm1 !=0 and elm2 !=0:
						if loc[1] != row: # skip diag (no recip.)
							ratio = elm2/elm1 # default
							self[loc] = ratio
							
	def getWeights(self, method='AHP'):
		
		if method=='AHP':
			"AHP prioritization. Normalized eigenvecs > select biggest real value"
			eva,eves=self._getEigen()
			eve_sum = sum(eves)
			return map(lambda v: v/eve_sum, eves) # in-place normalization
		
		else:
			"First normalize columns, then calculate row averages"
			self._normalize()
			return self._getRowAvgs()
			
	def getCR(self):
		return self._getCI() / self._getRI()
		
	def _getRowAvgs(self):
		"one-column (well,row) array of row averages."	
		return map(lambda x: sum(x)/len(self),self)
	def _traverseRatios(self,row=0):
		for i1 in range(self.shape[1]):
			if i1 != row: # skip current row
				for i2 in range(self.shape[1]):
						yield ( self[row,i1],self[row,i2], (i1,i2) )
						
	def _normalize(self):
		"Divide elements by column sums, making column sums become = 1"
		
		for c in range(len(self)):
			  self[:,c] = self[:,c] / sum(self[:,c])
			  
	def _traverseTriangle(self):
		"Traverses only upper-right triangle, excl. axis"
		height,width =self.shape
		for r in range(height):
			for c in range(r+1,width):
				yield (r,c)
				
	def __call__(self):
		for r in range(self.shape[0]):
			for c in range(self.shape[1]):
				print "%.3f" % self[r,c],
			print
			
		print "CR:%.4f, CI:%.4f, CR:%.4f" % (self.getCR(), self._getCI(),self._getRI())
		
	def _getEigen(self):
		"largest real eigenval & corresponding eigenvect."

		evas,eves = eigenvectors(self)
		curmax, curind = 0.0, 0
		
		for i in range(len(evas)):
			eva=evas[i]
			
			if type(eva) is complex:
				if eva.imag == 0 and eva.real > curmax:
					curmax=float(eva.real)
					curind=i
			elif eva > curmax: 
				curmax=float(eva)
				curind=i
	
		return curmax, map(lambda eve: abs(eve), eves[curind])
		
	def _getCI(self):
		"get Consistency Index"
		eva,eves = self._getEigen()
		n= len(self)
		return ( (eva-n) / (n-1) )
		
	def _getRI(self, calc=False):
		"Calculate avg. consistency index for a random array"
		
		# figures by Saaty
		
		if calc is False:
			vals=[0., 0., .52, .89, 1.11, 1.25, 1.35, 1.40, 1.45, 1.49]
			return vals[len(self)-1]
		
		else:
			tot=0.0
			ra = RatioArr(s=len(self))
		
			for c in range(calc):
				ra.randomize()
				tot += ra._getCI()
			
			return tot / calc
			

class DecisionSupportException(Exception):
	"base class for dss-related exceptions"
	def __init__(self, msg):
		self.msg=msg
		
	def __str__(self):
		return self.msg
		
class RatioWriteException(DecisionSupportException):
	"Fire if writing should cause an exception"
	def __init__(self, target, old):
		self.target = target
		self.old = old
		msg = "Target cell %s already has value %f (use 'force=True' to override)" % (self.target, self.old)
		DecisionSupportException.__init__(self,msg)
		
class RatioWriteError(DecisionSupportException):
	"fire if writing should cause an Error"
	def __init__(self, target):
		self.target = target
		msg = "Writing target cell (%i,%i) is not allowed!" % self.target
		DecisionSupportException.__init__(self,msg)
		
