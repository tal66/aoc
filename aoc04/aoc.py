from aoc04.aoc_input import s1, s2

e1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


# winning numbers | numbers you have

# numbers you have appear in the list of winning numbers.
# The first match makes the card worth 1 point
# each match after the first doubles the point value of that card


def aoc_1(input):
    sum = 0
    for line in input.split("\n"):
        line_parts = line.split("|")
        winning_nums = line_parts[0].split(": ")[1].split()
        your_nums = line_parts[1].split()
        row_sum = 0
        for num in your_nums:
            if num in winning_nums:
                if row_sum == 0:
                    row_sum = 1
                else:
                    row_sum *= 2
        sum += row_sum
    print(sum)
    return sum


def aoc_2(input):
    lines = input.split("\n")
    copies = [1 for _ in range(len(lines))]
    for idx, line in enumerate(lines):
        line_parts = line.split("|")
        winning_nums = line_parts[0].split(": ")[1].split()
        your_nums = line_parts[1].split()
        row_sum = 0
        matching_count = 0
        for num in your_nums:
            if num in winning_nums:
                matching_count += 1
                if row_sum == 0:
                    row_sum = 1
                else:
                    row_sum *= 2
        for i in range(1, matching_count + 1):
            if idx + i == len(copies):
                break
            copies[idx + i] += 1 * copies[idx]

        # sum += (row_sum * copies[idx])

    result = sum([int(n) for n in copies])
    print(result)
    return result


# aoc_1(e1) # 13
# aoc_1(s1)  # 26426

assert aoc_2(e1) == 30
assert aoc_2(s1) == 6227972
