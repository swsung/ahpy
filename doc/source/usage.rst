.. currentmodule:: ahpy.core

Usage
=====

The main AHP functionality resides in ahpy.core. There are two functions providing support for weight and consistency ratio calculation.

AHP is used on a problem roughly as follows:

Set up the criteria
------------------------------------

Set up the criteria (possibly including subcriteria). The criteria hierarchy is modeled simply as a tree of tuples where each tuple has:

 - the criteria and associated weights
 - the pairwise comparison data

The criteria and weights are stored as a recursive dictionary::

   {
      'id1': ( weight, {'subid11': weight, 'subid21': weight} ),
      'id2': ( weight, {'subid21': weight, 'subid22': weight} ),
      'id3': ( weight, {} )
   }


Select the alternatives to be considered
----------------------------------------

Compare criteria pairwise
-------------------------

The comparisons are stored as a list of (id, id, priority) tuples.


Assign criteria weights
-------------------------------------------------------------

The weights are calculated based on the pairwise comparisons of the criteria.

(see :func:`calculateWeights` in :mod:`ahpy.core`)


Compare alternatives pairwise
-----------------------------

Alternatives are compared with one another with respect to all criteria.

The comparisons are stored as a list of (id, id, priority) tuples.


Assign weights on alternatives
------------------------------

See :func:`ahpy.core.calculateWeights`


Review the result
------------------

The result is calculated according to the pairwise comparisons of the alternatives.

See :func:`ahpy.core.calculateConsistency`.

