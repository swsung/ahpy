"""Provides support for manipulating a simple criteria tree implementation using built-in datatypes.

The criteria and weights are stored as a simple recursive dictionary::

   {
      'id1': {'subid11': {}, 'subid21': {}},
      'id2': {'subid21': {}, 'subid22': {}},
      'id3': {}
   }

Thus a criteria element has subitems, whereas a criterion does not (empty dictionary).

"""

import sys
from string import join
from fractions import Fraction
from numpy import zeros

from ahpy.core import calculateWeights


class AHPError(Exception):
   "An error triggered by AHP-related problem"
   
   
def add_criterion(criteria, parent, name):
   """Add criterion to criteria, under parent (give None as parent to add to root).
   
   Examples:
   
   >>> c = {}
   >>> add_criterion(c, None, "a")
   {'a': {}}
   >>> add_criterion(c, "a", "a1")
   {'a': {'a1': {}}}
   
   """

   if not parent:
      criteria[name] = {}

   else:
      parent = find_criterion(criteria, parent)[parent]
      parent[name] = {}

   print criteria
      

def del_criterion(criteria, name):
   """Remove a named criterion.

   Examples:

   >>> c = {"a":{"a1":{},"a2":{}},"b":{}}
   >>> del_criterion(c, "a2")
   >>> del_criterion(c, "b")
   >>> print c
   {'a': {'a1': {}}}
   """

   try:
      del find_criterion(criteria, name)[name]
      logging.info("removed %s from criteria" % name)
   except:
      raise AHPError("no '%s' criterion in criteria" % name)

      
def find_criterion(criteria, name):
   """Return the parent criteria dict.

   Examples:

   >>> c = { "a": {"a1":{}}, "b":{} }
   >>> find_criterion(c, "a")
   {'a': {'a1': {}}, 'b': {}}
   >>> find_criterion(c, "a1")
   {'a1': {}}
   >>> find_criterion(c, "b")
   {'a': {'a1': {}}, 'b': {}}

   """

   if name in criteria:
      return criteria
   else:
      for k,v in criteria.items():
         try:
            c = find_criterion(v, name)
            if c:
               return c
         except:
            pass # no subitems
            
   return None


if __name__ == "__main__":
   import doctest
   doctest.testmod()
