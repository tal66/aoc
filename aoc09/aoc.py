from aoc09.aoc_input import s1, s2

e1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

e2 = """ """


def aoc_1(text_input):
    text_lines = text_input.splitlines()
    result = 0
    for line in text_lines:
        nums = line.split()
        nums = [int(n) for n in nums]

        diffs = get_diffs(nums)

        prev_last = 0
        for i in range(len(diffs) - 1, -1, -1):
            diff = diffs[i]
            last = diff[-1] + prev_last
            prev_last = last
            # print(f"i: {i} last: {last}")

        print(prev_last)
        result += prev_last
    print(result)
    return result


def get_diffs(nums):
    diffs = [nums]
    while True:
        curr = diffs[-1]
        diff = []
        for i in range(1, len(curr)):
            diff.append(curr[i] - curr[i - 1])

        # check if all 0
        flag = True
        for i in range(len(diff)):
            if diff[i] != 0:
                flag = False
                break

        if flag:
            break
        diffs.append(diff)
    return diffs


def aoc_2(text_input):
    text_lines = text_input.splitlines()
    result = 0
    for line in text_lines:
        nums = line.split()
        nums = [int(n) for n in nums]

        diffs = get_diffs(nums)
        # print(diffs)

        prev_last = 0
        for i in range(len(diffs) - 1, -1, -1):
            diff = diffs[i]
            last = diff[0] - prev_last
            prev_last = last
            # print(f"i: {i} last: {last}")

        print(prev_last)
        result += prev_last
    print(result)
    return result


# aoc_1(e1)  # 114
# aoc_1(s1)  # 1930746032


# aoc_2(e1) # 2
aoc_2(s1)  # 1154
