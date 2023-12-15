from aoc2022.aoc_input import s1

e1 = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def aoc_1(text_input):
    elves = get_elves(text_input)
    res = max(elves)
    print(res)
    return res


def aoc_2(text_input):
    elves = get_elves(text_input)
    elves.sort()
    res = elves[-3] + elves[-2] + elves[-1]
    print(res)
    return res


def get_elves(text_input):
    lines = text_input.splitlines()
    elves = []
    curr_sum = 0
    for line in lines:
        if line == "":
            elves.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)
    elves.append(curr_sum)

    return elves


assert aoc_1(e1) == 24000
assert aoc_1(s1) == 74394

assert aoc_2(e1) == 45000
aoc_2(s1) # 212836
