"Utility provisioning module"

from Interface import IInterface
from interfaces import *
from arraysupport import *

class UtilProvider:
	"provides utility using 1) AHP and 2) simple weighted average methods"
	
	__implements__= IUtilityProvider
	
	
	def __init__(self):
		self.strategies= []
		self.utilities= {}
		
	def setStrategy(self,strat):
		self.strategies.append(strat)
		strat.installInto(self)
		return len(self.strategies)-1
		
	def removeStrategy(self,id):
		try:
			self.strategies[id].removeFrom(self)
			del self.strategies[id]
		except:
			raise Exception, "No such strategy"
			
	def getStrategies(self):
		return self.strategies.keys()
		
	def addSink(self):
		for i in range(1, len(self.utilities)+1 ):
			if self.utilities.has_key(i):
				pass
			else:
				self.utilities.update( {i:None} )
			
		return i
		
	def removeSink(self,id):
		try:
			del self.utilities[id]
		except:
			raise Exception, "No such sink"
			

	def getSinks(self):
		return self.utilities.keys()
		
	def getUtility(self,id=None):
		if id is None:
			return self.utilities
		else:
			try:
				return self.utilities[id]
			except Exception, e:
				print e, "sink with id %i not found" % id
				

	def getUtilityUsing(self,strategy,id):
		return self.utilities[id]
		
	def _setUtility(self,id,ut):
		self.utilities.update( {id:ut} )
		
class RatioProviderStrategy(RatioArr):
	"A provider plug-in strategy"

	__implements__= IUtilityProviderStrategy
	
	def __init__(self):
		pass
		

	def sayHello(self):
		print "Hello World!"
		
	def installInto(self,uphost):
		uphost.sayHello = self.sayHello
	def removeFrom(self,uphost):
		del uphost.sayHello
		
		


