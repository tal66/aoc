from aoc08.aoc_input import s1, s2

e1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

e2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def aoc_1(text_input):
    lines = text_input.split("\n")
    instructions = lines[0]
    steps = 0
    d = build_dict(lines)

    print(d)

    curr = "AAA"
    idx = 0
    while True:
        if curr == "ZZZ":
            break
        steps += 1
        curr = d[curr][instructions[idx]]
        idx = (idx + 1) % len(instructions)

    print(steps)
    return steps


def build_dict(lines):
    d = {}
    for i in range(2, len(lines)):
        line = lines[i]
        line_parts = line.split(" = ")
        k = line_parts[0]
        values = line_parts[1].split(", ")
        left = values[0][1:4]
        right = values[1][0:3]
        d[k] = {"L": left, "R": right}
    return d


def aoc_2(text_input):
    lines = text_input.split("\n")
    instructions = lines[0]
    steps = 0
    d = build_dict(lines)
    # print(d)

    starting_nodes = []
    for k in d.keys():
        if k.endswith("A"):
            starting_nodes.append(k)

    idx = 0
    nodes_steps = {}
    while True:
        # check condition
        next_nodes = []
        for curr in starting_nodes:
            if curr.endswith("Z"):
                nodes_steps[curr] = steps
            else:
                next_nodes.append(curr)
        if len(next_nodes) == 0:
            break

        starting_nodes = next_nodes

        # update starting_nodes
        steps += 1
        next_nodes = []
        for node in starting_nodes:
            next_nodes.append(d[node][instructions[idx]])

        starting_nodes = next_nodes
        idx = (idx + 1) % len(instructions)

    print(f"nodes_steps: {nodes_steps}")
    print(f"steps: {steps}")

    import math
    result = math.lcm(*nodes_steps.values())
    print(result)
    return result


# aoc_1(e1) # 2
# aoc_1(e2) # 6
# aoc_1(s1)  # 17141


e3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

aoc_2(e3) # 6
# aoc_2(s1) # 10818234074807
