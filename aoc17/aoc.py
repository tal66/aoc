import inspect
from collections import namedtuple
from copy import deepcopy, copy
from queue import PriorityQueue

from aoc17.aoc_input import s1

e1 = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

"""
can move at most three blocks in a single direction
can't reverse
top-left to bottom-right
"""

Point = namedtuple("Point", "x y")
Directions = {"R": Point(1, 0), "L": Point(-1, 0), "U": Point(0, 1), "D": Point(0, -1)}
OpDirections = {"R": "L", "L": "R", "U": "D", "D": "U"}


class Player:
    max_streak = 3
    min_streak = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.curr_direction = ""
        self.curr_streak = 0
        # self.curr_sum = Player.to_grid_value(self.x, self.y)  # no
        self.curr_sum = 0
        self.possible_next_directions = self.possible_directions()

    def move(self, direction_key):
        if direction_key not in self.possible_next_directions:
            return
        prev_direction = self.curr_direction
        self.curr_direction = direction_key

        if prev_direction != direction_key:
            self.curr_streak = 0
        self.curr_streak += 1

        self.x, self.y = Player.add_direction(direction_key, self.x, self.y)
        row, col = self.to_grid_coord(self.x, self.y)
        self.curr_sum += int(grid[row][col])
        self.possible_next_directions = self.possible_directions()

    def possible_directions(self):
        result = []
        dir_keys = Directions.keys()
        if self.curr_streak < Player.min_streak and self.curr_direction:
            dir_keys = [self.curr_direction]

        for d in dir_keys:
            if not self.is_next_in_grid(d, self.x, self.y):
                continue
            if OpDirections.get(self.curr_direction) == d:
                continue
            if (self.curr_direction == d) and (self.curr_streak == Player.max_streak):
                continue
            result.append(d)
        return result

    @staticmethod
    def add_direction(d_key, x, y) -> (int, int):
        direction = Directions[d_key]
        next_x = x + direction.x
        next_y = y + direction.y
        return next_x, next_y

    @staticmethod
    def is_next_in_grid(d_key, x, y):
        if not d_key:
            return Player.is_in_grid(x, y)
        return Player.is_in_grid(*Player.add_direction(d_key, x, y))

    @staticmethod
    def is_in_grid(x, y):
        row, col = Player.to_grid_coord(x, y)
        in_grid = (0 <= col < len(grid[0]) and 0 <= row < len(grid))
        return in_grid

    @staticmethod
    def to_grid_value(x, y):
        row, col = Player.to_grid_coord(x, y)
        return int(grid[row][col])

    @staticmethod
    def is_done(player) -> bool:
        row, col = Player.to_grid_coord(player.x, player.y)
        end_pos = col == len(grid[0]) - 1 and row == len(grid) - 1
        return end_pos and player.curr_streak >= Player.min_streak

    @staticmethod
    def to_grid_coord(x, y):
        return -y, x

    def __hash__(self):
        c = self.code()
        return hash(c)

    def __eq__(self, other):
        return self.code() == other.code()

    def code(self):
        c = (self.x, self.y, self.curr_direction, self.curr_streak)
        return c

    def __lt__(self, other):
        return self.curr_sum < other.curr_sum


grid = []
visited = set()


def aoc_1(text_input):
    global grid, visited
    if inspect.stack()[1][3] != "aoc_2":
        Player.max_streak = 3
        Player.min_streak = 0

    lines = text_input.splitlines()
    grid = [list(line) for line in lines]

    player = Player(0, 0)
    visited = set()
    q = PriorityQueue()
    q.put(player)

    result = 10 ** 6

    while q.queue:
        player = q.get()

        if Player.is_done(player):
            result = player.curr_sum
            print(f"result: {result}")
            break

        if player in visited:
            continue

        for d in player.possible_next_directions:
            p = copy(player)
            p.move(d)
            q.put(p)

        visited.add(player)

    print(result)
    return result


def aoc_2(text_input):
    Player.max_streak = 10
    Player.min_streak = 4
    return aoc_1(text_input)


assert aoc_1(e1) == 102
# aoc_1(s1)  # 861

assert aoc_2(e1) == 94
e3 = """111111111111
999999999991
999999999991
999999999991
999999999991"""
assert aoc_2(e3) == 71

# aoc_2(s1)  # 1037
