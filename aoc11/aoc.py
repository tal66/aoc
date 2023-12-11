from bisect import bisect

from aoc11.aoc_input import s1, s2

e1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

e2 = """"""


# empty space (.) and galaxies (#)
# rows or columns that contain no galaxies should all be twice as big
# For each pair, find any shortest path between the two galaxies

def aoc_1(text_input):
    # expand
    lines = text_input.splitlines()
    lines = expand(lines)
    # for line in lines:
    #     print(''.join(line))

    # find galaxies
    galaxies = find_galaxies(lines)

    # distances
    result = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            dist = distance(galaxies[i], galaxies[j])
            result += dist

    print(result)
    return result


def find_galaxies(lines):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                galaxies.append([i, j])
    return galaxies


def distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def expand(lines: list):
    # find
    lines_to_expand = lines_to_expand_indices(lines)
    cols_to_expand = cols_to_expand_indices(lines)

    # expand
    # add cols
    lines_lists = []
    cols_to_expand = set(cols_to_expand)
    for i in range(len(lines)):
        line = lines[i]
        new_line = []
        for j in range(len(line)):
            if j in cols_to_expand:
                new_line.append('.')
            new_line.append(line[j])
        lines_lists.append(new_line)

    # add lines
    len_line = len(lines_lists[0])
    offset = 0
    for i in lines_to_expand:
        lines_lists.insert(i + offset, ['.' for _ in range(len_line)])
        offset += 1
    return lines_lists


###########################################

def cols_to_expand_indices(lines):
    cols_to_expand = []
    for j in range(len(lines[0])):
        all_dots = True
        for i in range(len(lines)):
            if lines[i][j] != '.':
                all_dots = False
                continue

        if all_dots:
            cols_to_expand.append(j)
    return cols_to_expand


def lines_to_expand_indices(lines):
    lines_to_expand = []
    for i, line in enumerate(lines):
        all_dots = True
        for c in line:
            if c != '.':
                all_dots = False
                continue

        if all_dots:
            lines_to_expand.append(i)
    return lines_to_expand


def row_dist(g1, g2, lines_to_expand, factor=2):
    n_rows = num_indices_in_range(g1, g2, lines_to_expand, 0)
    return abs(g1[0] - g2[0]) + n_rows * (factor - 1)


def col_dist(g1, g2, cols_to_expand, factor=2):
    n_cols = num_indices_in_range(g1, g2, cols_to_expand, 1)
    return abs(g1[1] - g2[1]) + n_cols * (factor - 1)


def num_indices_in_range(g1, g2, indices, idx=0):
    r1 = min(g1[idx], g2[idx])
    r2 = max(g1[idx], g2[idx])
    l1 = bisect(indices, r1)
    l2 = bisect(indices, r2)
    result = l2 - l1
    return result


def aoc_2(text_input, factor=2):
    lines = text_input.splitlines()
    galaxies = find_galaxies(lines)

    lines_to_expand = lines_to_expand_indices(lines)
    cols_to_expand = cols_to_expand_indices(lines)

    result = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            g1 = galaxies[i]
            g2 = galaxies[j]
            dist = row_dist(g1, g2, lines_to_expand, factor) + col_dist(g1, g2, cols_to_expand, factor)
            result += dist

    print(result)
    return result


# assert aoc_1(e1) == 374
# aoc_1(s1)  # 10231178


# assert num_indices_in_range([0, 0], [3, 1], [1, 2, 4, 5, 6, 7, 8]) == 2
# assert num_indices_in_range([1, 0], [3, 1], [2, 4, 5, 6, 7, 8]) == 1
# assert num_indices_in_range([1, 0], [3, 1], [4, 5, 6, 7, 8]) == 0
# assert num_indices_in_range([9, 0], [9, 9], [4, 5, 6, 7, 8], 1) == 5

assert aoc_2(e1, 2) == 374
assert aoc_2(e1, 10) == 1030
assert aoc_2(e1, 10 ** 2) == 8410

aoc_2(s1, 10 ** 6)  # 622120986954
