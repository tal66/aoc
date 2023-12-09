from aoc05.aoc_input import s1, s1_

e1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


# 7 maps
#  dest, src_start, length

class Map:
    def __init__(self, dest, src_start, length):
        self.dest = dest
        self.src_start = src_start
        self.src_end = src_start + length
        self.length = length

    def __repr__(self):
        return f"Map[dest: {self.dest}, ({self.src_start}, {self.src_end})]"


def parse_maps(text_input):
    lines = text_input.split("\n")
    maps = {}
    collection = []
    map_num = 0
    for i in range(2, len(lines)):
        if not lines[i]:
            maps[map_num] = collection
            map_num += 1
            collection = []
            continue
        if not lines[i][0].isdigit():
            continue
        curr = lines[i].strip().split(" ")
        dest, src_start, length = int(curr[0]), int(curr[1]), int(curr[2])
        collection.append(Map(dest, src_start, length))

    maps[map_num] = collection

    return maps


def aoc_1(text_input):
    lines = text_input.split("\n")
    seeds = lines[0].split(":")[1].strip().split(" ")
    seeds = [int(i) for i in seeds]
    print(seeds)

    maps = parse_maps(text_input)

    result = 1000000000000000000000000000000000
    for s in seeds:
        curr_seed = s
        print(f"curr_seed: {curr_seed}")
        for k in range(7):
            curr_map = maps[k]
            for m in curr_map:
                end_range = m.src_start + m.length
                if m.src_start <= curr_seed < end_range:
                    diff = (curr_seed - m.src_start)
                    curr_seed = m.dest + diff
                    break

        print(f"curr_seed: {curr_seed}")
        result = min(result, curr_seed)
    print(result)
    return result


##########################################################


def get_overlap(curr_seed, map):
    result = [-1, -1]
    # overlap of  (map.src_start, map.src_end) and (curr_seed[0], curr_seed[1])
    if map.src_start <= curr_seed[0] < map.src_end:
        result[0] = curr_seed[0]
    elif curr_seed[0] <= map.src_start:
        result[0] = map.src_start

    if map.src_start <= curr_seed[1] <= map.src_end:
        result[1] = curr_seed[1]
    elif map.src_end < curr_seed[1]:
        result[1] = map.src_end

    if result[0] == -1 or result[1] == -1:
        return [-1, -1]
    # print(f"get_overlap({curr_seed}, {map}): {result}")
    return result


def merge_overlaps(overlaps):
    # sort by start range, then end range
    overlaps.sort(key=lambda x: (x[0], x[1]))

    result = []
    for i in range(len(overlaps)):
        curr = overlaps[i]
        if curr[0] == -1:
            continue

        for j in range(i + 1, len(overlaps)):
            next = overlaps[j]
            if next[0] == -1:
                continue

            if curr[0] == next[0]:  # [0, 7] [0, 9] start same
                curr[1] = next[1]
                next[0] = -1
            elif curr[1] >= next[0]:  # [0, 9] [10, 12] end same
                curr[1] = next[1]
                next[0] = -1
            elif curr[1] >= next[1]:  # [0, 9] [6, 8] next ends before curr
                next[0] = -1
            else:
                break

        result.append(curr)
    return result


def get_not_overlaps(curr_seed, map_overlaps):
    if len(map_overlaps) == 0:
        return [curr_seed]

    result = []
    first_map_overlap = map_overlaps[0]
    if first_map_overlap[0] > curr_seed[0]:
        result.append([curr_seed[0], first_map_overlap[0]])

    prev = first_map_overlap
    for i in range(1, len(map_overlaps)):
        curr = map_overlaps[i]
        if curr[0] > prev[1]:
            result.append([prev[1], curr[0]])
        prev = curr

    last_map_overlap = map_overlaps[-1]
    if last_map_overlap[1] < curr_seed[1]:
        result.append([last_map_overlap[1], curr_seed[1]])

    # print(f"get_not_overlaps({curr_seed}  ,  {map_overlaps}): {result}")
    return result


def aoc_2(text_input):
    seeds = init_seeds(text_input)  # example: [[79, 93], [55, 68]] - range start, range end (exclusive)
    print(seeds)
    result = 1 << 40
    maps = parse_maps(text_input)
    print(f"maps: {len(maps)}")
    # print(f"maps: {maps}")

    for s in seeds:
        curr_seed = [s]
        print(f"================s in seeds: {curr_seed}")
        for k in range(len(maps)):
            curr_map = maps[k]
            curr_seed = next_seed_by_map(curr_seed, curr_map)
            # print(f"curr_seed: {curr_seed}")

        print(f"\ncurr_seed for s: {curr_seed} \n")
        result = min(result, curr_seed[0][0])
    print(f"result: {result}")
    return result


# assert aoc_1(e1) == 35
# assert aoc_1(s1) == 289863851

def next_seed_by_map(seeds, map):  # receives map paragraph
    print(f"\nnext_seed_by_map({seeds}) start")
    result = []
    overlaps = []  # of all seeds with map
    for s_ in seeds:
        next_seed = []
        # print(f"curr s_ in seeds: {s_}")
        for map_line in map:
            overlap = get_overlap(s_, map_line)
            if overlap[0] == -1:
                continue

            overlaps.append(overlap)
            dest_start = map_line.dest + (overlap[0] - map_line.src_start)
            overlap_len = (overlap[1] - overlap[0])
            next_seed.append([dest_start, dest_start + overlap_len])

        # print(f"next_seed before overlap added: {next_seed}")
        overlaps_merge = merge_overlaps(overlaps)

        not_overlaps = get_not_overlaps(s_, overlaps_merge)
        # print(f"overlaps: {overlaps}")
        # print(f"not_overlaps: {not_overlaps}")

        if len(not_overlaps) != 0:
            next_seed.extend(not_overlaps)

        next_seed = merge_overlaps(next_seed)
        next_seed.sort(key=lambda x: (x[0], x[1]))
        result.extend(next_seed)
        overlaps = []

    result.sort(key=lambda x: (x[0], x[1]))
    result = merge_overlaps(result)
    return result


def init_seeds(text_input):
    lines = text_input.split("\n")
    seeds_init = lines[0].split(":")[1].strip().split(" ")
    seeds = [int(i) for i in seeds_init]

    ranges = []

    for j in range(0, len(seeds), 2):
        init = seeds[j]
        end = init + seeds[j + 1]
        ranges.append([init, end])

    ranges = merge_overlaps(ranges)
    return ranges


assert aoc_2(e1) == 46
print()

aoc_2(s1)  # 60568880

e3 = """seeds: 5 7

seed-to-soil map:
8 5 3
10 10 2
20 4 1"""
# aoc_2(e3)

# overlaps: [[1, 3], [4, 5], [8, 10]]
# 1 2 | 4 | 8 9
# not_overlaps: [[3, 4], [5, 8], [10, 11]]
# 3 | 5 6 7 | 10
