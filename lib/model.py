"Decision-making model support"
import sys
from string import join
from numpy import array


def add_criterion(criteria, parent, name):
   "add criterion to criteria, under parent (give None as parent to add to root)"

   if not parent:
      criteria[name] = (0, {})

   else:
      parent = find_criterion(criteria, parent)[parent]
      parent[1][name] = (0, {})

   print criteria
      

def del_criterion(criteria, name):
   "remove a named criterion"

   try:
      del find_criterion(criteria, name)[name]
      print "removed %s" % name
   except:
      print "no '%s' criterion in criteria" % name

      
def find_criterion(criteria, name):
   "return the parent dict"

   if name in criteria:
      return criteria
   else:
      for k,v in criteria.items():
         try:
            c = find_criterion(v[1], name)
            if c:
               return c
         except:
            pass # no subitems
            
   return None
      


if __name__=="__main__":

   c = {"a":(0, {"a1":(0,{}),"a2":(0,{})}),"b":(2,{})}

   print "find b: ", find_criterion(c, "b")
   print "find a1: ", find_criterion(c, "a1")
   print "find z:", find_criterion(c, "z")

   print "remove a1"
   p = find_criterion(c, "a1")
   del p["a1"]
   print c

   del_criterion(c, "a2")
   print c

   del_criterion(c, "b")
   print c


   c = {}

   add_criterion(c, None, "a")
   add_criterion(c, None, "b")
   add_criterion(c, "a", "a1")
   add_criterion(c, "a", "a2")

   print "find b: ", find_criterion(c, "b")
   print "find a1: ", find_criterion(c, "a1")
   print "find z:", find_criterion(c, "z")

   print "remove a1"
   p = find_criterion(c, "a1")
   del p["a1"]
   print c

   del_criterion(c, "a2")
   print c

   del_criterion(c, "b")
   print c

