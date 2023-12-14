from dataclasses import dataclass

from aoc2022.aoc_input import s5

e1 = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


@dataclass
class Instruction:
    num: int
    from_: int
    to: int

    def __post_init__(self):
        self.num = int(self.num)
        self.from_ = int(self.from_)
        self.to = int(self.to)


def aoc_1(text_input, do_func):
    stacks_part, inst_part = text_input.split("\n\n")
    inst_part = inst_part.splitlines()

    inst = get_instructions(inst_part)
    stacks = get_stacks(stacks_part)

    do_func(inst, stacks)
    # print(stacks)

    result = "".join([s[-1] for s in stacks])
    print(f"result: {result}")
    return result


def get_instructions(inst_part):
    inst = []
    for i in inst_part:
        split = i.split()
        params = [split[idx] for idx in [1, 3, 5]]
        inst.append(Instruction(*params))
    return inst


def get_stacks(stacks):
    stacks = stacks.splitlines()
    num_stacks = int(stacks[-1][-2:-1])
    stacks_col = [[] for _ in range(num_stacks)]
    print(f"num_stacks = {num_stacks}")
    for i in range(num_stacks):
        for line in reversed(stacks[:-1]):
            c = line[i * 4 + 1]
            if c != " ":
                stacks_col[i].append(c)

    return stacks_col


def do(inst, stacks):
    for i in inst:
        for _ in range(i.num):
            pop = stacks[i.from_ - 1].pop()
            stacks[i.to - 1].append(pop)


def do_ord(inst, stacks):
    for i in inst:
        chars = []
        for _ in range(i.num):
            pop = stacks[i.from_ - 1].pop()
            chars.append(pop)
        for c in reversed(chars):
            stacks[i.to - 1].append(c)


def aoc_2(text_input, do_func=do_ord):
    return aoc_1(text_input, do_func)


aoc_1(e1, do)  # CMZ
aoc_1(s5, do)  # PSNRGBTFT

aoc_2(e1, do_ord)  # MCD
aoc_2(s5, do_ord)  # BNTZFPMMW
