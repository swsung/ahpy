"Set up the test running environment and run the tests"

import sys
import unittest

import testcases as tc

def runGUIMode(tmod,tclass):
	try:
		from unittestgui import tk, TkTestRunner
		root = tk.Tk()
		root.title("PyUnit")
		runner = TkTestRunner(root, tmod.__name__ + '.'+tclass.__name__)
		root.protocol('WM_DELETE_WINDOW', root.quit)
		root.mainloop()
	
	except:
		print "Could not run tests in GUI. PyUnit not installed?"
		

def runTextMode(tmod,tclass):
	
	l = unittest.defaultTestLoader
	suite = l.loadTestsFromModule(tmod)

	print "Following tests will be run:"
	print "----------------------------------------------------------------------"
	for c in l.getTestCaseNames(tclass):
		print c

	runner=unittest.TextTestRunner()
	runner.run(suite)
	


try:
	runTextMode(tc,tc.RA_TestCase)
	runTextMode(tc,tc.UP_TestCase)

	# runGUIMode()
	
except Exception, e:
	print e
	
