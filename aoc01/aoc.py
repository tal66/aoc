from aoc01.aoc_input import s

e1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

valid_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def aoc1_1(s: str) -> int:
    result = 0
    lines = s.splitlines()
    for line in lines:
        left = 0
        right = len(line) - 1

        while not line[left].isdigit():
            left += 1

        while not line[right].isdigit():
            right -= 1

        n = line[left] + line[right]
        result += int(n)

    print(result)
    return result


def aoc1_2(s: str) -> int:
    result = 0
    for line in s.splitlines():
        left_num = get_left_num(line)
        right_num = get_right_num(line)

        if left_num == 0:
            left_num = right_num
        elif right_num == 0:
            right_num = left_num

        # print(f"{left_num} {right_num}")
        n = left_num * 10 + right_num
        result += int(n)
    print(result)
    return result


def get_left_num(line):
    left = 0
    left_word = ""
    left_num = 0
    while left < len(line):
        if line[left].isdigit():
            left_num = int(line[left])
            break
        else:
            left_word += line[left]
            n = from_dict(left_word, "left")
            if n != -1:
                left_num = n
                break
            else:
                left += 1

    return left_num


def get_right_num(line):
    right = len(line) - 1
    right_word = ""
    right_num = 0

    while right >= 0:
        if line[right].isdigit():
            right_num = int(line[right])
            break
        else:
            right_word = line[right] + right_word
            n = from_dict(right_word, "right")
            if n != -1:
                right_num = n
                break
            else:
                right -= 1

    return right_num


def from_dict(s: str, left_or_right) -> int:
    start_idx = len(s) - 5
    is_left = (left_or_right == "left")

    for i in range(start_idx, len(s) - 2):
        if is_left:
            sub = s[i:len(s)]
        else:
            sub = s[0:len(s) - i]
        if sub in valid_digits:
            return valid_digits[sub]

    return -1


e2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

assert aoc1_1(e1) == 142
assert aoc1_1(s) == 54940
assert aoc1_2(e2) == 281
assert aoc1_2(s) == 54208


def testing():
    assert aoc1_2("15nine1") == 11
    assert aoc1_2("7877pzrbtcsddmrffzdsmqlqkjsix") == 76
    assert aoc1_2("5four3eight") == 58
    assert aoc1_2("fourhzgxqtxggfpprrmtfqsdhc2fdxnjdgx64five") == 45
    assert aoc1_2("threeninejdzzrbpmfhjcqdsix8two2bb") == 32
    assert aoc1_2("1148pdtcl1eight5oneights") == 18
    assert aoc1_2("5fivekxfzpzjsd42sevenzgfourtwo") == 52
    assert aoc1_2("5dncccmkpqtwocmmlltvbg") == 52
    assert aoc1_2("dbmxvpsvp7jdnvsdnlv") == 77


testing()
