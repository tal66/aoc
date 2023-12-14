import collections

from aoc2022.aoc_input import s6

e1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


def aoc_1(text_input, N=4):
    ll = collections.deque()
    freq = dict()

    for i, c in enumerate(text_input, start=1):
        if len(ll) < N:
            ll.append(c)
            freq[c] = freq.get(c, 0) + 1
            continue

        pop = ll.popleft()
        if freq[pop] > 1:
            freq[pop] -= 1
        else:
            del freq[pop]

        ll.append(c)
        freq[c] = freq.get(c, 0) + 1

        if len(freq) == N:
            print(i)
            return i

    print(f"not found")


def aoc_2(text_input):
    return aoc_1(text_input, N=14)


assert aoc_1(e1) == 7
assert aoc_1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert aoc_1("nppdvjthqldpwncqszvftbrmjlhg") == 6

aoc_1(s6)  # 1356

assert aoc_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
assert aoc_2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
aoc_2(s6)  # 2564
