from aoc10.aoc_input import s1, s2

import sys

sys.setrecursionlimit(10 ** 4 * 5)

e1 = """.....
.S-7.
.|.|.
.L-J.
....."""

e2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position
"""

right = [0, 1]
left = [0, -1]
up = [-1, 0]
down = [1, 0]
d = {"|": [up, down], "-": [left, right],
     "L": [up, right], "J": [up, left], "7": [down, left], "F": [right, down],
     ".": [], "S": [], "*": [], }


class Position:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def __repr__(self):
        return f"Pos[{self.row} {self.col}]"

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def copy(self) -> "Position":
        return Position(self.row, self.col)

    def copy_from(self, other) -> None:
        self.row = other.row
        self.col = other.col

    def add(self, direction):
        self.row += direction[0]
        self.col += direction[1]

    def legal(self, lines):
        return 0 <= self.row < len(lines) and 0 <= self.col < len(lines[0])


def aoc_1(text_input):
    lines = text_input.splitlines()
    lines = [list(line) for line in lines]
    start_pos = set_start(lines)
    print(f"start: {start_pos}  direction: {d['S']}")
    return get_circle(lines, start_pos)


def get_circle(lines, start):
    pos = start.copy()
    nodes = visit(lines, start, pos, [])

    c = len(nodes)
    if c == -1:
        print("no circle")
        return []

    print(f"nodes: {len(nodes)} result: {c / 2}")
    return nodes


def visit(lines, start_pos, pos, curr_nodes=[]):
    if pos == start_pos and len(curr_nodes) > 2:
        return curr_nodes

    org_symbol = lines[pos.row][pos.col]
    if org_symbol in ["V", "."]:
        return []

    org_pos = pos.copy()
    lines[pos.row][pos.col] = "V"
    curr_nodes.append(org_pos)
    directions = d[org_symbol]

    for direction in directions:
        pos.copy_from(org_pos)
        pos.add(direction)

        if not pos.legal(lines):
            continue

        if lines[pos.row][pos.col] == ".":
            continue

        result_nodes = visit(lines, start_pos, pos, curr_nodes)
        if 0 < len(result_nodes):
            return result_nodes

    pos.copy_from(org_pos)
    lines[pos.row][pos.col] = org_symbol
    curr_nodes.pop()

    return curr_nodes


def set_start(lines) -> Position or None:
    d["S"] = []
    row_col = None

    # find
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                row_col = [i, j]
                break

    if row_col is None:
        return None

    start_pos = Position(row_col[0], row_col[1])
    pos = start_pos.copy()

    # set directions
    directions = [left, right, up, down]
    for direction in directions:
        pos.copy_from(start_pos)
        pos.add(direction)
        if not pos.legal(lines):
            continue

        neighbor_pos = pos.copy()
        neighbor_symbol = lines[pos.row][pos.col]
        neighbor_directions = d[neighbor_symbol]
        for neighbor_direction in neighbor_directions:
            pos.add(neighbor_direction)
            if pos == start_pos:
                d["S"].append(direction)
            pos.copy_from(neighbor_pos)

    return start_pos


assert len(aoc_1(e1)) / 2 == 4
assert len(aoc_1(e2)) / 2 == 8
assert len(aoc_1(s1)) / 2 == 6649

e3 = """LJF7
--SL"""
# aoc_1(e3)  #


e4 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

# part 2
# my solution for part 2: after spacing the graph, there's at least one neighboring node to S which is inside the loop
# so i'm flooding from there, and check out the count (loop nodes were already found in part 1)
# made it run fast on the large input, but it requires choosing from 8 values (which can be automated), so not uploading

