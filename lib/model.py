"Decision-making model support"
import sys
from string import join
from numpy import array


def add_criterion(criteria, parent, name):
   """Add criterion to criteria, under parent (give None as parent to add to root).

   Examples:
   
   >>> c = {}
   >>> add_criterion(c, None, "a")
   {'a': (0, {})}
   >>> add_criterion(c, "a", "a1")
   {'a': (0, {'a1': (0, {})})}

   """

   if not parent:
      criteria[name] = (0, {})

   else:
      parent = find_criterion(criteria, parent)[parent]
      parent[1][name] = (0, {})

   print criteria
      

def del_criterion(criteria, name):
   """Remove a named criterion.

   >>> c = {"a":(0, {"a1":(0,{}),"a2":(0,{})}),"b":(2,{})}
   >>> del_criterion(c, "a2")
   removed a2
   >>> del_criterion(c, "b")
   removed b
   >>> del_criterion(c, "z")
   no 'z' criterion in criteria
   >>> print c
   {'a': (0, {'a1': (0, {})})}
   """

   try:
      del find_criterion(criteria, name)[name]
      print "removed %s" % name
   except:
      print "no '%s' criterion in criteria" % name

      
def find_criterion(criteria, name):
   """Return the parent criteria dict.

   >>> c = { "a": (0,{"a1":(0,{})}), "b":(0,{}) }
   >>> find_criterion(c, "a")
   {'a': (0, {'a1': (0, {})}), 'b': (0, {})}
   >>> find_criterion(c, "a1")
   {'a1': (0, {})}
   >>> find_criterion(c, "b")
   {'a': (0, {'a1': (0, {})}), 'b': (0, {})}

   """

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
      


if __name__ == "__main__":

    import doctest
    doctest.testmod()

