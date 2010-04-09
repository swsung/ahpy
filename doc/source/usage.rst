.. currentmodule:: ahpy.core

Usage
=====

The main AHP functionality resides in ahpy.core. There are two functions providing support for weight and consistency ratio calculation.

AHP is used on a problem roughly as follows:

Set up the criteria
-------------------

Set up the criteria (possibly including subcriteria).

(see :mod:`ahpy.model`)


Choose the alternatives to be considered
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

