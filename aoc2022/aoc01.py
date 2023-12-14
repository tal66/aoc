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
    lines = text_input.splitlines()
    max_elf = 0
    curr_sum = 0
    for line in lines:
        if line == "":
            if curr_sum > max_elf:
                max_elf = curr_sum
            curr_sum = 0
        else:
            curr_sum += int(line)

    print(max_elf)


def aoc_2(text_input):
    lines = text_input.splitlines()
    max_elf = []
    curr_sum = 0
    for line in lines:
        if line == "":
            max_elf.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)

    max_elf.append(curr_sum)
    max_elf.sort()

    res = max_elf[-3] + max_elf[-1] + max_elf[-2]
    print(res)
    return res


# aoc_1(e1) #
# aoc_1(s1) # 74394

assert aoc_2(e1) == 45000
aoc_2(s1)
