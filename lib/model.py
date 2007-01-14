"Decision-making model support"import sys
from string import join
app = sys.path.append
app('/tmp/lib/python2.2/site-packages')
app('/tmp/lib/python2.2/site-packages/numarray')
app('/tmp')

from gnosis.xml import objectify as obify
from numarray import array
import pyRXP

class Alternatives(obify._XO_,dict):
   def __str__(self):
      alts=[]
      
      for a in self.alternative:
         alts.append(a.name)
      return join(alts,", ")
   
   def getRatios(self):
      R=[]
      for a in self.alternative:
         try:
            for r in a.ratio:
               print r.to,r.PCDATA
         except:
            pass
            
class Criteria(obify._XO_):
   def __str__(self):
      cri=[]
      for a in self.criterion:
         cri.append(a.name)
      return join(cri,", ")
      
class Model(obify._XO_):
   def __str__(self):
      alts="Alternatives: %s\n" % self.alternatives
      cri= "Criteria: %s\n" % self.criteria
      return alts+cri

obify._XO_model=Model
obify._XO_alternatives=Alternatives
obify._XO_criteria=Criteria

model=obify.XML_Objectify( 'model.xml' ).make_instance()
