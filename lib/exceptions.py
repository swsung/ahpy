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
		
