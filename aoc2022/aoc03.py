from aoc2022.aoc_input import s3

e1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def aoc_1(text_input):
    lines = text_input.splitlines()
    result = 0
    for line in lines:
        chars = set()
        m = int(len(line) / 2)
        item1, item2 = line[:m], line[m:]
        for i in range(m):
            chars.add(item1[i])

        for i in range(m):
            if item2[i] in chars:
                result += priority(item2[i])
                break
    print(result)
    return result


def priority(c: str):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c.lower()) - ord('a') + 27


assert priority('A') == 27


def aoc_2(text_input):
    lines = text_input.splitlines()
    result = 0
    for i in range(0, len(lines), 3):
        chars1 = set([c for c in lines[i]])
        chars2 = set([c for c in lines[i + 1]])

        for c in lines[i + 2]:
            if c in chars1 and c in chars2:
                result += priority(c)
                break
    print(result)
    return result


# aoc_1(e1) # 157
# aoc_1(s3)  # 7737

# assert aoc_2(e1) == 70
aoc_2(s3)  # 2697
