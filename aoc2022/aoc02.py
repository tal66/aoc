from aoc2022.aoc_input import s2

e1 = """A Y
B X
C Z"""

d = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def aoc_1(text_input):
    result = 0
    lines = text_input.splitlines()
    for line in lines:
        round = line.split(" ")
        score = get_score(round)
        result += (score + d[round[1]])
    print(result)
    return result


def get_score(round):
    a, b = round

    if d[a] == d[b]:
        return 3

    if b == "X" and a == "C":
        return 6
    if a == "A" and b == "Z":
        return 0

    if d[a] < d[b]:
        return 6
    return 0


def aoc_2(text_input):
    result = 0
    lines = text_input.splitlines()

    for line in lines:
        round = line.split(" ")
        score = get_score2(round)
        result += score

    print(result)
    return result


"""
X means you need to lose, 
Y means you need to end the round in a draw, 
Z means you need to win.

(1 for Rock, 2 for Paper, and 3 for Scissors)
1 < 2 < 3 < 1 ...
"""

game = [1, 2, 3]
d2 = {"X": "lose", "Y": "draw", "Z": "win"}

def get_score2(round):
    op = d[round[0]]
    end = round[1]

    if d2[end] == "draw":
        return 3 + op

    if d2[end] == "win":
        idx = game.index(op)
        resp = game[(idx + 1) % len(game)]
        return 6 + resp

    if d2[end] == "lose":
        idx = game.index(op)
        resp = game[(idx - 1) % len(game)]
        return 0 + resp

    return None

# aoc_1(e1) # 15
# aoc_1(s2)  # 12740

assert aoc_2(e1) == 12
aoc_2(s2) # 11980
