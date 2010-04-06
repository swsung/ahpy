"Decision-making model support"
import sys
from string import join

from numpy import array


def model2array(model):
   "convert model comparison data into a numpy array for weight calculation"

   alternatives = ["apple", "banana", "cherry"]

   criteria = {
      "color": 0,
      "taste": 0,
      "health":0,
   }

   """   
   comparisons = {
     ("color", "health", 3),
     ("color", "taste",  4),
     ("taste", "health", 5)
   }
   """

def weight2model(weights, model):
   "copy weights into the model data structure"





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


