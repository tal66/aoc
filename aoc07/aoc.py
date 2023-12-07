from aoc07.aoc_input import s1, s2

e1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

""" part 1:
A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
"""
d = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}

""" part 2:
A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J
"""
d2 = {"A": 1, "K": 2, "Q": 3, "T": 4, "9": 5, "8": 6, "7": 7, "6": 8, "5": 9, "4": 10, "3": 11, "2": 12, "J": 13}

"""
Every hand is exactly one type. From strongest to weakest, they are:
1 5: AAAAA
2 4,1: AA8AA
3 3,2: 23332
4 3,1,1: TTT98
5 2,2,1: 23432
6 2,1,1,1: A23A4
7 distinct: 23456
"""


def get_hand_rank(hand):
    count = {}
    for c in hand:
        if count.get(c):
            count[c] += 1
        else:
            count[c] = 1

    if len(count) == 1:
        result = 1
    elif len(count) == 2:
        if 4 in count.values():
            result = 2
        else:
            result = 3
    elif len(count) == 3:
        if 3 in count.values():
            result = 4
        else:
            result = 5
    elif len(count) == 4:
        result = 6
    else:
        result = 7

    return result


class Hand:

    def __init__(self, hand, bid, rank) -> None:
        self.hand = hand
        self.bid = bid
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.hand} {self.bid} {self.rank}"


def aoc_1(text_input, rank_func=get_hand_rank, d=d):
    lines = text_input.split("\n")
    hands = []

    for line in lines:
        hand = line.split(" ")[0]
        bid = line.split(" ")[1]
        hands.append(Hand(hand, int(bid), rank_func(hand)))

    # sort by rank, secondarily by the dict d value
    hands.sort(key=lambda x: (x.rank, [d[c] for c in x.hand]))
    # print(hands)

    result = 0
    l = len(hands)
    for i, h in enumerate(hands, start=1):
        result += h.bid * (l - i + 1)

    print(result)


def get_hand_rank2(hand):
    if "J" not in hand:
        return get_hand_rank(hand)

    count = {}
    for c in hand:
        if count.get(c):
            count[c] += 1
        else:
            count[c] = 1

    j_count = hand.count("J")
    if j_count == 5:
        return get_hand_rank(hand)
    del count["J"]
    max_count_key = max(count, key=count.get)

    return get_hand_rank(hand.replace("J", max_count_key))


def aoc_2(text_input):
    aoc_1(text_input, get_hand_rank2, d2)


# aoc_1(e1) # 6440
# aoc_1(s1)  # 251121738


aoc_2(e1)  # 5905
aoc_2(s1)  # 251421071
