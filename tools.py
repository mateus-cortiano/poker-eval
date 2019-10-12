from itertools import combinations


def output_all_hands(file):
    #          2     3     4     5     6     7     8     9     T     J     Q      K    A
    VALUES = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
    SUITS = ['s', 'h', 'd', 'c']
    cards = []

    for value in VALUES:
        for suit in SUITS:
            cards.append(value + suit)

    dump = open(file, "w")
    dump.write('\n'.join(''.join(_) for _ in combinations(cards, 6)))
    dump.close



def hand_sorter(hand):
    VALUES_IT = [0, 4, 8, 12, 16]
    cards = {}
    for d in VALUES_IT:
        cards.update({hand[d]\
                    + hand[d+1]\
                    + hand[d+2]\
                    : int(hand[d]\
                    + hand[d+1])})
    sorted_cards = sorted(cards.items(), reverse=True)
    return(" ".join("".join(k) for k, _ in sorted_cards))


output_all_hands("output.txt")


# flushes = open("hands_flushes.txt", "w")
# nonflushes = open("hands_nonflushes.txt", "w")
# all_hands = 'all_hands_sorted.txt'
# with open(all_hands, "r") as ah:
#     line = ah.readline()
#     cnt = 1
#     while line:
#         if evaluate_hand(line.strip()):
#             flushes.write(line.strip() + "\n")
#         else:
#             nonflushes.write(line.strip() + "\n")
#         line = ah.readline()
#         # cnt += 1
#         # if cnt > 20:
#         #     break