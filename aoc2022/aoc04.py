from aoc2022.aoc_input import s4

e1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def aoc_1(text_input):
    lines = text_input.splitlines()
    result = 0

    for line in lines:
        split = line.split(",")
        a = split[0].split("-")
        b = split[1].split("-")
        a = [int(x) for x in a]
        b = [int(x) for x in b]

        if a[0] <= b[0] and b[1] <= a[1]:
            result += 1
        elif b[0] <= a[0] and a[1] <= b[1]:
            result += 1

    print(result)
    return result


def aoc_2(text_input):
    lines = text_input.splitlines()
    result = 0

    for line in lines:
        split = line.split(",")
        a = split[0].split("-")
        b = split[1].split("-")
        a = [int(x) for x in a]
        b = [int(x) for x in b]

        if a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]:
            result += 1
        elif b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]:
            result += 1

    print(result)
    return result


aoc_1(e1)  # 2
aoc_1(s4)  # 562

assert aoc_2(e1) == 4
aoc_2(s4) # 924
