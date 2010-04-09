Introduction
============

The module provides support for the following AHP-related tasks:

 - building and reviewing the criteria hierarchy
 - setting up the list of alternatives
 - doing pairwise comparisons
 - calculating the priorities
 - reviewing the consistency ratio (CR)   

The scope of the library is intentionally kept small. 

It implements the necessary AHP algorithms and provides rudimentary support for managing the criteria, set of alternatives, the pairwise comparisons and the weights.

These are all loosely coupled to maintain a clean separation between the model, the pairwise comparisons and the calculation of weights.
