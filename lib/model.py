"Decision-making model support"
import sys
from string import join

from numpy import array

class Alternatives(dict):
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
            
class Criteria:
   def __str__(self):
      cri=[]
      for a in self.criterion:
         cri.append(a.name)
      return join(cri,", ")
      
class Model:
   def __str__(self):
      alts="Alternatives: %s\n" % self.alternatives
      cri= "Criteria: %s\n" % self.criteria
      return alts+cri


