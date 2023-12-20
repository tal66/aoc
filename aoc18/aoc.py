from collections import namedtuple
import sys

sys.setrecursionlimit(10 ** 4 * 5)
from aoc18.aoc_input import s1

e1 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

e2 = """ """

Point = namedtuple("Point", "x y")
Directions = {"R": Point(1, 0), "L": Point(-1, 0), "U": Point(0, 1), "D": Point(0, -1)}


class Player:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.curr_direction = ""
        self.visited = {(self.x, self.y)}

    def move(self, direction_key):
        self.curr_direction = direction_key
        self.x, self.y = Player.add_direction(direction_key, self.x, self.y)
        self.visited.add((self.x, self.y))

    @staticmethod
    def add_direction(d_key, x, y, n_steps=1) -> (int, int):
        direction = Directions[d_key]
        next_x = x + direction.x * n_steps
        next_y = y + direction.y * n_steps
        return next_x, next_y


def aoc_1(text_input, start_f):
    lines = text_input.splitlines()
    player = Player(0, 0)

    for line in lines:
        direction, n_steps, color = line.split(" ")
        n_steps = int(n_steps)
        for _ in range(n_steps):
            player.move(direction)

    print(len(player.visited))
    grid, converted_visited = make_grid(player.visited)

    flood(grid, start_f, converted_visited)
    count = count_grid(grid)
    print(count)

    return count


def print_grid(grid_):
    print(f"grid: {len(grid_)}x{len(grid_[0])}")
    for i, row in enumerate(grid_):
        print("".join(row))
    print()


def count_grid(grid):
    count = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col != ".":
                count += 1
    return count


def make_grid(visited):
    min_x, min_y = min(p[0] for p in visited), min(p[1] for p in visited)
    max_x, max_y = max(p[0] for p in visited), max(p[1] for p in visited)

    grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    converted_visited = []
    for x, y in visited:
        converted_visited.append((y - min_y, x - min_x))

    for x, y in converted_visited:
        grid[x][y] = '#'

    return grid, converted_visited


def flood(grid, p, visited):
    r, c = p
    if not (0 <= c < len(grid[0]) and 0 <= r < len(grid)):
        return
    if (r, c) in visited or grid[r][c] == "#":
        return

    grid[r][c] = "#"
    flood(grid, (r, c + 1), visited)
    flood(grid, (r, c - 1), visited)
    flood(grid, (r + 1, c), visited)
    flood(grid, (r - 1, c), visited)


########################

def aoc_2(text_input):
    lines = text_input.splitlines()
    d = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

    p1 = (0, 0)
    result = 1
    for line in lines:
        _, _, color = line.split(" ")
        color = color[2:-1]
        n_steps, direction = color[:-1], color[-1]
        n_steps, direction = int(n_steps, 16), d[direction]

        p2 = Player.add_direction(direction, *p1, n_steps)

        # result += (p2[1] + p1[1]) * (p2[0] - p1[0]) / 2
        result += (p2[0] * p1[1] - p1[0] * p2[1]) / 2
        result += n_steps / 2

        p1 = p2

    print(result)
    return result


# (manually select inner point)
# aoc_1(e1, (1,3))  # 62
# aoc_1(s1, (58, 42))  # 35401

# (formula)
assert aoc_2(e1) == 952408144115
aoc_2(s1)  # 48020869073824
