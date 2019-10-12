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
    dump.write('\n'.join(''.join(_) for _ in combinations(cards, 5)))
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


# Mass Evaluator
# dump = "E:\\Dump\\dump2.txt"
# file = "output.txt"
# with open(file, "r") as f:
#     line = f.readline()
#     cnt = 1
#     start_time = datetime.now()
#     with open(dump, "a") as d:
#         d.write(str(start_time) + "\n")
#         while line:
#             d.write(str(evaluate_hands(line.strip())) + "\n")
#             line = f.readline()
#         d.write(str(datetime.now() - start_time))