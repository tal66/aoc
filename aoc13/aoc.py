from aoc13.aoc_input import s1

e1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

e2 = """#...##..#
#....#..#
..##..###
#####.##.
#####.##."""


def parse(text_input):
    items = text_input.split("\n\n")
    for item in items:
        lines = item.split("\n")
        lines = [list(line) for line in lines]
        yield lines


def transpose(lines):
    columns = []
    for i in range(len(lines[0])):
        col = [line[i] for line in lines]
        columns.append(col)
    return columns


def aoc_1(text_input):
    items = parse(text_input)
    result = 0
    for line_group in items:
        result += calculate(line_group)

    print(f"result: {result}")
    return result


def calculate(lines):
    r = row_ref(lines)
    if r > 0:
        return r * 100

    c = row_ref(transpose(lines))
    return c


def row_ref(lines):  # return reflect row num
    for i in range(1, len(lines)):
        if one_row_ref(lines, i):
            return i
    return -1


def one_row_ref(lines, i) -> bool:  # around row i
    up = i - 1
    down = i
    while up >= 0 and down < len(lines):
        if not (lines[up] == lines[down]):
            return False
        up -= 1
        down += 1

    return True


#################


"""exactly one . or # should be the opposite type"""


def aoc_2(text_input):
    items = parse(text_input)
    result = 0
    for line_group in items:
        result += s_calculate(line_group)

    print(f"result: {result}")
    return result


def s_calculate(lines):
    # rows
    for i in range(len(lines)):
        r = row_ref_d(lines)
        if r > 0:
            # print(f"r {r}")
            return r * 100

    # cols
    lines_t = transpose(lines)
    for i in range(len(lines_t)):
        r = row_ref_d(lines_t)
        if r > 0:
            # paint(lines_t)
            # print(f"c {r}")
            return r

    exit(1)


def row_ref_d(lines):
    for i in range(1, len(lines)):
        if around_row_count_d(lines, i) == 1:
            return i
    return -1


def around_row_count_d(lines, i) -> int:
    diff_count = 0
    up = i - 1
    down = i
    while up >= 0 and down < len(lines):
        line_u = lines[up]
        line_d = lines[down]
        diff_count += count_diff_two_lines(line_d, line_u)
        up -= 1
        down += 1

    return diff_count


def count_diff_two_lines(line_d, line_u):
    return sum([1 if line_u[j] != line_d[j] else 0 for j in range(len(line_u))])


def paint(lines):
    for line in lines:
        print("".join(line))


assert aoc_1(e1) == 405
assert aoc_1(s1) == 27502

e3 = """....#..
###....
...#.##
###....
....##.
##.#.##
..##.##
###.#..
..#.###"""

assert aoc_2(e1) == 400
assert aoc_2(e2) == 100
assert aoc_2(e3) == 6
assert aoc_2(s1) == 31947
