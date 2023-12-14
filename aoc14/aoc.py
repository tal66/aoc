from enum import Enum

from aoc14.aoc_input import s1

e1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

e2 = """ """

"""
(O) will roll when the platform is tilted, 
(#) will stay in place
"""


def aoc_1(text_input):
    lines = text_input.splitlines()
    s_rocks = [0 for _ in range(len(lines[0]))]
    result = 0
    len_col = len(lines)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                s_rocks[j] = i + 1
            if c == "O":
                result += len_col - s_rocks[j]
                s_rocks[j] += 1

    print(f"result: {result}")
    return result


##########################

"""
cycle - north, west, south, east
"""


class RockType(Enum):
    Round, Cube = range(1, 3)

    def __str__(self):
        return "O" if self == RockType.Round else "#"


def aoc_2(text_input):
    grid = init_grid(text_input)
    d = {}
    s = -1
    diff = -1
    for i in range(1, 300):
        grid = move(grid)
        g = printed_grid(grid)
        if g in d:
            s = d[g]
            diff = i - s
            print(f"{i} == {d[g]}")
            break
        d[g] = i
    assert s != -1

    a = 1000000000 - s
    m = a % diff
    grid = init_grid(text_input)
    for i in range(s + m):
        grid = move(grid)
    # aoc_1(printed_grid(grid)) # can't use because tilt

    result = 0
    len_col = len(grid[0])
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == RockType.Round:
                result += len_col - i

    print(f"result2: {result}")
    return result


def init_grid(text_input):
    lines = text_input.splitlines()
    grid: list[list] = [[None for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == str(RockType.Round):
                grid[i][j] = RockType.Round
            elif c == str(RockType.Cube):
                grid[i][j] = RockType.Cube
    return grid


def move(grid):
    grid = move_up(grid)
    grid = move_left(grid)
    grid = move_down(grid)
    grid = move_right(grid)
    return grid


def printed_grid(grid):
    p = []
    for line in grid:
        l = "".join(["." if not i else str(i) for i in line])
        p.append(l)
    return "\n".join(p)


def print_grid(grid):
    print(f"\ngrid: {len(grid)}x{len(grid[0])}")
    print(printed_grid(grid))


def move_up(grid):
    d = [0 for _ in range(len(grid))]
    for i, line in enumerate(grid):
        for j, r in enumerate(line):
            if not r:
                continue

            if r == RockType.Round:
                if d[j] == i:
                    d[j] += 1
                else:
                    grid[d[j]][j] = r
                    d[j] += 1
                    line[j] = None
            else:
                d[j] = i + 1
    return grid


def move_down(grid):  # slow
    grid = move_up(list(reversed(grid)))
    return list(reversed(grid))


def move_left(grid):
    for i, line in enumerate(grid):
        move_line_left(line)
    return grid


def move_line_left(line):
    d = 0
    for j, r in enumerate(line):
        if not r:
            continue
        if r == RockType.Round:
            if d == j:
                d += 1
            else:
                line[d] = r
                d += 1
                line[j] = None
        else:
            d = j + 1
    return line


def move_right(grid):  # slow
    for i, _ in enumerate(grid):
        line = move_line_left(list(reversed(grid[i])))
        grid[i] = list(reversed(line))
    return grid


# assert aoc_1(e1) == 136
# assert aoc_1(s1) == 108955


e1_1 = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#...."""

e1_2 = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O"""

g = move(init_grid(e1))
assert printed_grid(g) == e1_1
g = move(g)
assert printed_grid(g) == e1_2

aoc_2(e1)  # 64
aoc_2(s1)  # 106689
