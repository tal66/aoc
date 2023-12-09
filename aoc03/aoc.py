from aoc03.aoc_input import s1, s2

# any number adjacent to a symbol, even diagonally,
# is a "part number" and should be included
e1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def aoc_1(input):
    sum = 0
    lines = input.split("\n")

    for i in range(len(lines)):
        curr_num_str = ""
        curr_flag = False

        line = lines[i]
        for j in range(len(line)):
            if line[j].isdigit():
                curr_num_str += line[j]
                if is_num_near_symbol(lines, i, j):
                    # print(f"{lines[i][j]} {i} {j}")
                    curr_flag = True
            else:
                if curr_flag:
                    if not curr_num_str == "":
                        sum += int(curr_num_str)

                curr_flag = False
                curr_num_str = ""

        if curr_flag:
            if not curr_num_str == "":
                sum += int(curr_num_str)
                # print(curr_num_str)

    print(sum)
    return sum


def aoc_2(input):
    sum = 0
    lines = input.split("\n")
    len_line = len(lines[0])

    for i in range(len(lines)):
        for j in range(len_line):
            if lines[i][j] != "*":
                continue
            sum += gear_ratio(lines, i, j)

    print(sum)
    return sum


def gear_ratio(lines, i, j):
    if i == 0 or i == len(lines) - 1:
        return 0

    a = get_adjacent(lines[i - 1], j)
    b = get_adjacent(lines[i + 1], j)
    c = get_adjacent_same_line(lines[i], j)

    num_list = a + b + c
    if len(num_list) != 2:
        return 0

    return num_list[0] * num_list[1]


def get_adjacent_same_line(line, j):
    # doesn't include j
    result = []
    if j < len(line) and line[j + 1].isdigit():
        num = ""
        idx = j + 1
        while idx < len(line) and line[idx].isdigit():
            num += line[idx]
            idx += 1
        result.append(int(num))

    if j > 0 and line[j - 1].isdigit():
        num = ""
        idx = j - 1
        while idx >= 0 and line[idx].isdigit():
            num = line[idx] + num
            idx -= 1
        result.append(int(num))

    return result


def get_adjacent(line, j):
    result = []
    # include j
    if line[j].isdigit():
        num = line[j]
        idx = j + 1
        while idx < len(line) and line[idx].isdigit():
            num += line[idx]
            idx += 1

        idx = j - 1
        while idx >= 0 and line[idx].isdigit():
            num = line[idx] + num
            idx -= 1
        result.append(int(num))
        return result

    # doesn't include j
    result.extend(get_adjacent_same_line(line, j))

    return result


def is_num_near_symbol(lines, i, j):
    c = lines[i][j]
    if c == ".":
        return False
    if not c.isdigit():
        return False

    len_line = len(lines[i])

    # prev line
    if i > 0 and is_num_in_adj_line(lines[i - 1], j):
        return True

    # next line
    if i < len_line - 1 and is_num_in_adj_line(lines[i + 1], j):
        return True

    # same line
    line = lines[i]
    if j > 0 and is_symbol(line[j - 1]):
        return True
    if j < len_line - 1 and is_symbol(line[j + 1]):
        return True

    return False


def is_num_in_adj_line(line, j):
    len_line = len(line)

    if is_symbol(line[j]):
        return True
    if j > 0 and is_symbol(line[j - 1]):
        return True
    if j < len_line - 1 and is_symbol(line[j + 1]):
        return True
    return False


def is_symbol(c: str):
    if c == ".":
        return False
    if c.isdigit():
        return False
    return True


assert aoc_1(e1) == 4361
assert aoc_1(s1) == 530849

assert aoc_2(e1) == 467835
assert aoc_2(s1) == 84900879
