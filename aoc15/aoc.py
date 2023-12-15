from collections import deque
from dataclasses import dataclass

from aoc15.aoc_input import s1

e1 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def aoc_1(text_input):
    steps = text_input.split(",")
    result = 0
    for step in steps:
        result += hash_(step)
    print(result)
    return result


def hash_(step):
    result = 0
    for c in step:
        result += ord(c)
        result *= 17
        result %= 256
    return result


#####################

@dataclass
class Lens:
    label: str
    focal_len: int

    def __repr__(self):
        return f"Lens({self.label})"


class Box:
    def __init__(self):
        self.lenses = deque()
        self.labelsToLens = {}

    def add_lens(self, label, focal_len):
        if self.contains(label):
            self.labelsToLens[label].focal_len = focal_len
        else:
            new_lens = Lens(label, focal_len)
            self.lenses.append(new_lens)
            self.labelsToLens[label] = new_lens

    def contains(self, label):
        return label in self.labelsToLens

    def rm_lens(self, label):
        if not self.contains(label):
            return
        lens = self.labelsToLens[label]
        self.lenses.remove(lens)  # o(n)
        self.labelsToLens.pop(label)

    def __repr__(self):
        return f"Box({self.lenses})"


def aoc_2(text_input):
    steps = text_input.split(",")
    boxes: list[Box or None] = [None for _ in range(256)]

    for step in steps:
        do_step(step, boxes)

    # print(f"{boxes}")
    result = 0
    for box_num, b in enumerate(boxes, start=1):
        if not b:
            continue
        for slot_num, l in enumerate(b.lenses, start=1):
            result += box_num * slot_num * l.focal_len

    print(result)
    return result


def do_step(step, boxes):
    op = "=" if "=" in step else "-"
    label, v = step.split(op)
    box_num = hash_(label)
    curr_box = boxes[box_num]

    if op == "-":
        if curr_box:
            curr_box.rm_lens(label)
    elif op == "=":
        if curr_box is None:
            curr_box = Box()
            boxes[box_num] = curr_box
        curr_box.add_lens(label, int(v))


# assert hash_("cm-") == 253
# assert aoc_1(e1) == 1320
# aoc_1(s1)  # 503154

aoc_2(e1)  # 145
aoc_2(s1)  # 251353
