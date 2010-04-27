"""Provides support for manipulating a simple criteria tree implementation,
using built-in datatypes.

The criteria is stored as a simple recursive dictionary::

   {
      'id1': {'subid11': {}, 'subid21': {}},
      'id2': {'subid21': {}, 'subid22': {}},
      'id3': {}
   }

Thus a criteria element has subitems, whereas a criterion is an empty dict.

"""

class AHPModelError(Exception):
   "An error triggered by AHP-related problem"
   
   
def add_criterion(criteria, parent, name):
   """Add criterion to a parent criterion; give None to add to root.
   
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

   >>> c = {"a1":{},"a2":{},"b":{}, "c":{}}
   >>> del_criterion(c, "a2")
   >>> del_criterion(c, "b")
   >>> print c
   {'a1': {}, 'c': {}}
   """

   parent = find_criterion(criteria, name)
   if parent:
      del parent[name]
   else:
      raise AHPModelError("no such criterion: %s" % name)

      
def find_criterion(criteria, name):
   """Return the parent criteria dict.

   Examples:

   >>> c = {"a":{"a1":{}}, "b":{} }
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
      for key, val in criteria.items():
         cri = find_criterion(val, name)
         if cri:
            return cri
            
   return None


def traverse(criteria, label="criteria", level=1):
   """Return a generator to traverse the criteria and assign weights.
   
   An example:
   
   >>> cri = {
   ... "a1":{"a21":{},"a22":{}},
   ... "b1":{"b21":{"b31":{}, "b32":{}}, "b22":{}}
   ... }
   >>> for sub in traverse(cri):
   ...   print sub
   ('a1', {'a21': {}, 'a22': {}})
   ('b21', {'b31': {}, 'b32': {}})
   ('b1', {'b22': {}, 'b21': {'b31': {}, 'b32': {}}})
   ('criteria', {'a1': {'a21': {}, 'a22': {}}, 'b1': {'b22': {}, 'b21': {'b31': {}, 'b32': {}}}})
   """
   
   for key, value in criteria.items():   
      if value:
         for subitem in traverse(value, key, level+1):
            yield subitem
   level -= 1
   yield (label, criteria, level)


if __name__ == "__main__":
   import doctest
   doctest.testmod()
