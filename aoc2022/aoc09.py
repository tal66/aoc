from collections import namedtuple

from aoc2022.aoc_input import s9

e1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

e2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

Motion = namedtuple("Motion", "direction dist")
Point = namedtuple("Point", "x y")
Directions = {"R": Point(1, 0), "L": Point(-1, 0), "U": Point(0, 1), "D": Point(0, -1)}


class Player:
    def __init__(self, x=0, y=0, name="", tail=None):
        self.x = x
        self.y = y
        self.tail = tail
        self.name = name
        self.visited: set = {Point(x, y)}

    def move(self, directions):
        # print(f"{self.name} moving {directions}")
        for direction in directions:
            d = Directions[direction]
            self.x += d.x
            self.y += d.y
        if self.tail:
            self.tail.notify(Point(self.x, self.y))
        self.visited.add(Point(self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    @staticmethod
    def near(p1, p2):
        return abs(p1.x - p2.x) <= 1 and abs(p1.y - p2.y) <= 1

    def notify(self, parent_p):
        if Player.near(self, parent_p):
            return

        if parent_p.x == self.x:  # same row
            if parent_p.y > self.y + 1:
                self.move("U")
            elif parent_p.y < self.y + 1:
                self.move("D")
        elif parent_p.y == self.y:  # same col
            if parent_p.x > self.x + 1:
                self.move("R")
            elif parent_p.x < self.x + 1:
                self.move("L")
        else:
            self._move_tail_diag(parent_p)

        if self.tail:
            self.tail.notify(Point(self.x, self.y))

    def _move_tail_diag(self, p):
        if p.x > self.x:
            if p.y > self.y:
                self.move("RU")
            else:
                self.move("RD")
        else:
            if p.y > self.y:
                self.move("LU")
            else:
                self.move("LD")


class State:
    tail = Player()
    head = Player(tail=tail)

    @staticmethod
    def reset(tail_len=1):
        if tail_len < 1:
            State.tail = None
            State.head = Player(name="H")
            return

        State.tail = Player(name=str(tail_len))
        prev = State.tail
        curr = None
        for i in range(tail_len):
            curr = Player(tail=prev, name=str(tail_len - i - 1))
            prev = curr
        State.head = curr
        State.head.name = "H"


def get_motions(text_input):
    lines = text_input.splitlines()
    for line in lines:
        direction, dist = line.split()
        yield Motion(direction, int(dist))


def print_grid(size=10):
    off = size // 2
    print()
    grid = [["." for _ in range(size)] for _ in range(size)]
    c = State.head
    while c:
        grid[c.y + off][c.x + off] = c.name
        c = c.tail
    for p in State.tail.visited:
        grid[p.y + off][p.x + off] = "X"
    for row in reversed(grid):
        print("".join(row))


def aoc_1(text_input):
    State.reset()

    motions = get_motions(text_input)
    for m in motions:
        for _ in range(m.dist):
            State.head.move(m.direction)

    # print(State.tail.visited)
    result = len(State.tail.visited)
    print(result)
    # print_grid()
    return result


def aoc_2(text_input):
    State.reset(tail_len=9)

    motions = get_motions(text_input)
    for m in motions:
        for _ in range(m.dist):
            State.head.move(m.direction)

    result = len(State.tail.visited)
    try:
        print_grid(35)
    except IndexError:
        pass

    print(f"result: {result} tail: {State.tail.name}")
    return result


# assert aoc_1(e1)  == 13
# assert aoc_1(s9)  == 5907

aoc_2(e1)
assert aoc_2(e2) == 36
# aoc_2(s9) # 2303
