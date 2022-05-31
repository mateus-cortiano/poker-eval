""" utils.py """

from itertools import combinations

# ---


def output_all_hands(file):
    VALUES = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
    ]
    SUITS = ["s", "h", "d", "c"]
    cards = []

    for value in VALUES:
        for suit in SUITS:
            cards.append(value + suit)

    dump = open(file, "w")
    dump.write("\n".join("".join(_) for _ in combinations(cards, 6)))
    dump.close


def hand_sorter(hand):
    VALUES_IT = [0, 4, 8, 12, 16]
    cards = {}
    for d in VALUES_IT:
        cards.update({hand[d] + hand[d + 1] + hand[d + 2]: int(hand[d] + hand[d + 1])})
    sorted_cards = sorted(cards.items(), reverse=True)
    return " ".join("".join(k) for k, _ in sorted_cards)
