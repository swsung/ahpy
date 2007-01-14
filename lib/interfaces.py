"Package interfaces"

import sys
# sys.path.append('/home/petri/dev')
sys.path.append('/net/homes/u008/saffe/dev')


from Interface import IInterface

class IUtilityProvider(IInterface):
	"component for utility provisioning."
	
	def setStrategy(strat):
		"add a new strategy (object), return id of the strategy"
		
	def removeStrategy(id):
		"remove a strategy with given id"
		
	def getUtility(id=None):
		"get utility for sink, or if id is not given, an array of (id,utility) pairs"
		
	def getUtilityUsing(id):
		"get utility using strategy with id"
		
	def addSink():
		"add a new sink, return id of the new sink"
		
	def removeSink(id):
		"remove a sink"
		
	def setUtility(id):
		"set utility for a sink"
		
	def getSinks():
		"get list of sinks' id's"
		
class IUtilityProviderStrategy(IInterface):
	"determines utility within the component"
	
	def installInto():
		"have plugin install itself"
		
	def removeFrom():
		"make plugin remove itself"
		
