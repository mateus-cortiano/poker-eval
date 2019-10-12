"""=== EQUITY CALCULATOR ==="""

from hand_evaluator import evaluate_hands
from holdem_range import HoldemRange
from random import shuffle


def GetEquity(iter, *hands, board=[]):

    """
    Returns the equity for two or more players

    Arguments:
        :iter: Number of iterations

        :*hands: Hands in the format [[13, "s"], ...]

        :board: You need want some part of the board
                already dealt
    """

    deck = [[x, y] for x in range(13, 0, -1) for y in ["s", "h", "d", "c"]]
    for card in [x[k] for x in hands for k in range(0,2)]:
        deck.remove(card)
    for card in board:
        deck.remove(card)

    wins = {i:0 for i in range(len(hands))}

    for _ in range(0, iter):
        rem_deck = deck[:]
        shuffle(rem_deck)
        rem_board = board[:]
        for _ in range(len(board), 5):
            rem_board += [rem_deck.pop()]
        player_arr = [(hands.index(hand), hand + rem_board) for hand in hands]
        eval = evaluate_hands(array=player_arr)
        for (player, value) in eval.m_carlo:
            wins[player] += value
    return {k:round(v*0.5/iter, 4) for (k,v) in wins.items()}

def GetEquityVsRange(iter, hero, range, board=[]):

    """
    Returns the equity for a given combo vs
    a given range of combos

    Arguments:
        :iter: Number of iterations

        :hero: Hand to return the equity in the format:
               [[int, suit], [int, suit]]

        :range: The range that the hero cards will play
                against. This argument must be a 
                HoldemRange() dictionary.
        
        :board: You need want some part of the board
                already dealt
    """

    for (combo, freq) in range.combos.items():
        vs_hand = [[int(combo[0:2]), combo[2]], [int(combo[3:5]), combo[5]]]
        if any(hero == villain for hero in hero for villain in vs_hand):
            continue
        elif freq == 0:
            continue
        else:
            equity = GetEquity(iter, hero, vs_hand, board=board)
            if 'final_equity' in locals():
                final_equity = (final_equity + equity[0]) / 2
            else:
                final_equity = equity[0]
    return final_equity

range_bb = HoldemRange(1)


# hands = []
# hands.insert(0, [[10, 'c'], [9, 'd']])            
# hands.insert(1, [[13, 'c'], [12, 's']])
# hands.insert(2, [[13, 'd'], [12, 'h']])

board = []

print(GetEquityVsRange(10, [[10, 'd'], [9, 'd']], range_bb))