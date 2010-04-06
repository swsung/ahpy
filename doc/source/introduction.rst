Introduction
============

The module provides support for the following AHP-related tasks:

 - building and reviewing the criteria hierarchy
 - setting up the list of alternatives
 - doing pairwise comparisons
 - calculating the priorities
 - reviewing the consistency ratio (CR)   

The library maintains a clean separation between the model, the pairwise comparisons and the calculation of weights.

The hierarchy is modeled simply as a tree of tuples where each tuple has:

 - the criteria and associated weights
 - the pairwise comparison data

The criteria and weights are stored as a recursive dictionary::

   {
      id1: ( [ (subid11, weight), (subid21, weight) ], weight ),
      id2: ( [ (subid21, weight), (subid22, weight) ], weight ),
   }

The comparisons are stored as a list of (id, id, priority) tuples.

