from collections import namedtuple, deque

from aoc16.aoc_input import s1

e1 = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

e2 = """ """

Point = namedtuple("Point", "x y")
Directions = {"R": Point(1, 0), "L": Point(-1, 0), "U": Point(0, 1), "D": Point(0, -1)}
symbol_map = {"/": {"R": "U", "L": "D", "U": "R", "D": "L"},
              "\\": {"R": "D", "L": "U", "U": "L", "D": "R"},
              ".": {"R": "R", "L": "L", "U": "U", "D": "D"},
              "|": {"U": "U", "D": "D"},
              "-": {"R": "R", "L": "L"}
              }


class Beam:
    def __init__(self, x=0, y=0, curr_direction="R", name="0"):
        self.x = x
        self.y = y
        self.curr_direction = curr_direction
        self.visited = set()
        self.name = name
        self.state = 1

    def move(self):
        if self.state == 0:
            return
        symbol = self.get_symbol()
        if not symbol:
            self.shutdown()
            return

        next_d = symbol_map[symbol].get(self.curr_direction, "")
        if symbol in [".", "/", "\\"]:
            self.curr_direction = next_d
            self.move_in_curr_direction()
        elif symbol in ["-", "|"]:
            if next_d:
                self.curr_direction = next_d
                self.move_in_curr_direction()
            else:
                self.shutdown()
                if self.curr_direction in "LR" and symbol == "|":
                    d1, d2 = ("U", "D")
                elif self.curr_direction in "UD" and symbol == "-":
                    d1, d2 = ("L", "R")
                else:
                    print(f"error")
                    return
                b1 = Beam(self.x, self.y, curr_direction=d1, name=f"{self.name}{d1}")
                b2 = Beam(self.x, self.y, curr_direction=d2, name=f"{self.name}{d2}")
                beams.extend((b1, b2))
                b1.move()
                b2.move()

    def move_in_curr_direction(self):
        if self.get_mem_code() in visited_in_direction:
            self.shutdown()
            return

        d = Directions[self.curr_direction]
        self.visited.add((self.x, self.y))
        visited_in_direction.add(self.get_mem_code())
        self.x += d.x
        self.y += d.y

    def get_mem_code(self):
        return f"{self.x},{self.y},{self.curr_direction}"

    def get_symbol(self):
        x = self.x
        y = -self.y
        if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
            self.shutdown()
            return ""
        return grid[y][x]

    def shutdown(self):
        self.state = 0
        # print(f"bye {self.name}")

    def __repr__(self):
        return f"B({self.name})"


grid = []
beams = []
visited_in_direction = set()


def aoc_1(text_input, start_beam=Beam(0, 0)):
    global grid, beams, visited_in_direction
    lines = text_input.splitlines()
    grid = [[c for c in line] for line in lines]
    beams = []
    visited_in_direction = set()

    beam = start_beam
    beams.append(beam)

    visited = set()
    for i in range(2000):
        # print(beams)
        for beam in beams:
            beam.move()
            visited.update(beam.visited)

        if len([b for b in beams if not b.state]) == len(beams):
            # print(f"stop after {i}")
            break

    result = len(visited)

    # paint(grid, visited)

    print(result)
    return result


def paint(grid, visited):
    for p in visited:
        grid[-p[1]][p[0]] = "#"
    for line in grid:
        print("".join(line))


def aoc_2(text_input):
    lines = text_input.splitlines()
    m, n = len(lines), len(lines[0])
    result = 0

    for j in range(m):
        r = aoc_1(text_input, start_beam=Beam(0, -j))
        result = max(result, r)
        r = aoc_1(text_input, start_beam=Beam(n - 1, -j, curr_direction="L"))
        result = max(result, r)

    print("\ntrying cols")
    for i in range(m):
        r = aoc_1(text_input, start_beam=Beam(i, 0, curr_direction="D"))
        result = max(result, r)
        r = aoc_1(text_input, start_beam=Beam(i, -(n - 1), curr_direction="U"))
        result = max(result, r)

    print(f"\nresult: {result}")
    return result


# assert aoc_1(e1) == 46
# aoc_1(s1)  # 7870

# aoc_2(e1)  # 51
aoc_2(s1)  # 8143
