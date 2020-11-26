"""=== HAND EVALUATOR ==="""

from collections import Counter

# Globals

STRAIGHTS = [
    sorted([13, *range(1,14)][n:n+5]) for n in range(0,10)
]

class evaluate_hands():

    """
    Evaluates best 5 to 7 card hands between
    a maximum of 9 players and returns their ranks
    in order from best to worst hand.

    Arguments:
        :*hands: The hand from each player in the format:
                 [[int, suit], [int, suit]] for every hand

        :array: More suitable to pass multiple players hands
    """ 

    def __init__(self, *hands, array=""):

        # Creating key value pair for player:hand

        ranking = []
        if array:
            self.players = [(player, hand) for player, hand in enumerate(array)]
        else:
            self.players = [sorted(arg) for arg in hands]

        # Evaluating every player hand and returning its absolute rank

        for player, hand in enumerate(self.players):

            rank = [1] + [i[0] for i in sorted(hand, reverse=True)][0:5]

            # Pairs +

            pairs = self.eval_pairs(hand)
            if pairs:
                rank = pairs
            
            # Straights and Flushes

            flush = self.eval_flush(hand)
            straight = self.eval_straight(hand)

            if straight:
                if flush:
                    rank = [9, straight]
                else:
                    rank = [5, straight]
            elif flush:
                    rank = [6] + flush

            # Final hand rank

            ranking.append([rank, player])
        
        # Final ranking

        ranking.sort(reverse=True)

        if ranking[0][0] == ranking [1][0]:
            ranking[0].insert(0, 1)
            for n in range(1, len(ranking)):
                if ranking[n][0] == ranking[n-1][1]:
                    ranking[n].insert(0, 1)
                    continue
                else:
                    ranking[n].insert(0, 0)
        else:
            ranking[0].insert(0, 2)
            for n in range(1, len(ranking)):
                ranking[n].insert(0, 0)
            
        self.m_carlo = [(x[2], x[0]) for x in ranking]


    def eval_flush(self, hand):

        """ Evaluates flushes """

        cnt = Counter(x for list in hand for x in list[1])
        vset = list(cnt.values())

        if any(i >= 5 for i in vset):
            return [i[0] for i in sorted(hand, reverse=True) if i[1] == [k for k in cnt if cnt[k] > 4][0]][0:5]
        else:
            return False


    def eval_straight(self, hand):

        """ Evaluates straights """

        vset = sorted([i[0] for i in hand])
        if max([len(set(vset).intersection(set(s))) for s in STRAIGHTS]) >= 5:
            return [max(i) for i in [set(vset).intersection(set(s))\
                    for s in STRAIGHTS] if len(i) > 4][-1]
        else:
            return False


    def eval_pairs(self, hand):

        """ Evaluates if there's and how much pairs, trips and quads """

        vset = Counter([i[0] for i in hand])
        if any(i > 1 for i in vset.values()):

            quads = {k:v for (k, v) in vset.items() if v > 3}
            if quads:
                v1 = max(list(quads.keys()))
                vset.pop(v1)
                return [8, v1, sorted(list(vset.keys()), reverse=True)]

            pairs = {k:v for (k, v) in vset.items() if 1 < v < 3}
            trips = {k:v for (k, v) in vset.items() if 2 < v < 4}

            if trips:
                if pairs:
                    v1 = max(list(trips.keys()))
                    v2 = max(list(pairs.keys()))
                    vset.pop(v1)
                    vset.pop(v2)
                    return [7, v1, v2]
                else:
                    v1 = max(list(trips.keys()))
                    vset.pop(v1)
                    return [4, v1] + sorted(list(vset.keys()), reverse=True)[0:2]

            if pairs:
                if len(pairs) > 1:
                    v1 = max(list(pairs.keys()))
                    pairs.pop(v1)
                    v2 = max(list(pairs.keys()))
                    vset.pop(v1)
                    vset.pop(v2)
                    return [3, v1, v2, sorted(list(vset.keys()), reverse=True)[0]]
                else:
                    v1 = max(list(pairs.keys()))
                    pairs.pop(v1)
                    vset.pop(v1)
                    return [2, v1] + sorted(list(vset.keys()), reverse=True)[0:3]

        return False