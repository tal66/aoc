import math
import re

from aoc12.aoc_input import s1, s2

e1 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

e2 = """ """

"""
operational (.) or damaged (#)
how many different arrangements
"""


############### bf

def aoc_1_bf(text_input):
    lines = text_input.splitlines()
    result = 0

    for i, line in enumerate(lines):
        split = line.split()
        record = split[0]  # "???.###"
        record = [c for c in record]

        nums = split[1].split(",")
        nums = [int(n) for n in nums]  # [1,1,3]

        result += bf(record, nums)

    print(result)
    return result


def bf(record, nums) -> int:
    if "?" not in record:
        if check_translation(record, nums):
            return 1
        else:
            return 0

    result = 0
    i = record.index("?")

    record[i] = "#"
    result += bf(record, nums)
    record[i] = "."
    result += bf(record, nums)
    record[i] = "?"

    return result


def check_translation(record: list, nums: list) -> bool:
    idx = 0
    i = 0
    while i < len(record):
        count = 0
        c = record[i]
        while c == "#":
            count += 1
            i += 1
            if i == len(record):
                break
            c = record[i]

        if count > 0:
            if idx == len(nums):
                return False
            if count != nums[idx]:
                return False
            idx += 1
            i -= 1
        i += 1

    return idx == len(nums)


############### fast

class Mem:
    d = {}

    def __init__(self, nums_idx, record_idx, curr_count):
        self.nums_idx = nums_idx
        self.record_idx = record_idx
        self.curr_count = curr_count

    def __eq__(self, other):
        return self.nums_idx == other.nums_idx and self.record_idx == other.record_idx and self.curr_count == other.curr_count

    def __hash__(self):
        return hash((self.nums_idx, self.record_idx, self.curr_count))

    def __repr__(self):
        return f"Mem({self.nums_idx}, {self.record_idx}, {self.curr_count})"


def aoc_1(text_input, M=1):
    lines = text_input.splitlines()
    result = 0

    for line in lines:
        Mem.d = {}
        split = line.split()
        record = split[0]  # "???.###"
        record = "?".join([record] * M)

        nums = split[1].split(",")
        nums = [int(n) for n in nums]  # [1,1,3]
        nums = nums * M

        result += dp(record, nums, 0, 0, 0)

    print(result)
    return result


def dp(record, nums, nums_idx, record_idx, curr_count):
    if record_idx == len(record):
        if nums_idx == len(nums) and curr_count == 0:
            return 1
        elif nums_idx == len(nums) - 1 and curr_count == nums[nums_idx]:
            return 1
        else:
            return 0

    if nums_idx < len(nums) and curr_count > nums[nums_idx]:
        return 0
    if nums_idx >= len(nums) and curr_count > 0:
        return 0

    mem = Mem(nums_idx, record_idx, curr_count)
    if mem in Mem.d:
        return Mem.d[mem]

    result = 0
    if record[record_idx] in ["#", "?"]:
        result += dp(record, nums, nums_idx, record_idx + 1, curr_count + 1)

    if record[record_idx] in [".", "?"]:
        if nums_idx < len(nums) and curr_count == nums[nums_idx]:
            result += dp(record, nums, nums_idx + 1, record_idx + 1, 0)
        elif 0 < curr_count < nums[nums_idx]:
            result += 0
        else:
            result += dp(record, nums, nums_idx, record_idx + 1, 0)

    Mem.d[mem] = result
    return result


def aoc_2(text_input):
    return aoc_1(text_input, 5)


# assert aoc_1("???.### 1,1,3") == 1
# assert aoc_1(".??..??...?##. 1,1,3") == 4
# assert aoc_1("?#?#?#?#?#?#?#? 1,3,1,6") == 1
# assert aoc_1("????.#...#... 4,1,1") == 1
# assert aoc_1("???.##.# 1,2,1") == 3
# assert aoc_1("????.######..#####. 1,6,5") == 4
# assert aoc_1("?###???????? 3,2,1") == 10
#
# assert aoc_1_bf(e1) == 21
# assert aoc_1_bf(s1) == 7705

assert aoc_1(e1) == 21
assert aoc_1(s1) == 7705

aoc_2(s1)  # 50338344809230
