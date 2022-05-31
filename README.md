# poker-eval
a python poker hand evaluator

- hand_evaluator.py:
  this is the base of the project.
  it takes one to nine lists of hands that represents the players in the format [[face, suit], ...]
then returns an ordered ranking of every hand, even in the case of draws.

- equity_calculator.py:
  this is used to calculate the equity of two Texas Hold'em hands.
  it can receive just the pair of hands as well as some board cards (flop, turn or river).
  we have two functions in this one, GetEquity() and GetEquityVsRange().
  GetEquity returns the equity between two exact hands.
  GetEquityVsRange returns the equity of a single hand vs a range of hands.
  both of these calls the hand_evaluator.py main function, save the results and calculate
the equity in monte-carlo style.
  we can use both to calculate a range vs range situation, calling the GetEquityVsRange for every card
in one of the ranges.

#

  I ultimately gave up this project because of performance issues.
  Since this is my first real python project I'm just leaving it on GitHub for the memories.
  Python is just too slow, and there are other libraries that are already fast and reliable.
  My goal is to rewrite this in C or C++.
