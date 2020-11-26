"""=== HOLDEM RANGE ==="""

from itertools import combinations

class HoldemRange(list):

    """
    Creates a dictionary with every possible
    no order combination of every two cards as keys
    and assigns a frequency value to every one of them.

    Arguments:
        :freq: in decimals, is the frequency of the combo
               in the list. Default is 0.
    """

    def __init__(self, freq=0):
        deck = [str(x).zfill(2)+y for x in range(13, 0, -1) for y in ["s", "h", "d", "c"]]
        self.combos = {"".join(k):freq for k in list(combinations(deck,2))}
        pass


    def SetAllFreq(self, freq):
        """ Function to set all the combos to a passed frequency """
        self.combos.update({k:freq for k in self.combos})


    def SetComboFreq(self, combo, freq):
        """ Sets the frequency for a specific combo """
        if combo in self.combos.keys():
            self.combos.update({combo:freq})
        else:
            if combo[3:6] + combo[0:3] in self.combos.keys():
                self.combos.update({combo[3:6] + combo[0:3]:freq})
            else:
                print('Not valid combo')


    def DumpRange(self, file):
        """ Dumps the range to a file """
        with open(file, "w") as f:
            f.write("\n".join(["{0}: {1}".format(k, f) for [k, f] in self.combos]))