from aoc2022.aoc_input import s8

e1 = """30373
25512
65332
33549
35390"""


def aoc_1(text_input):
    global mem_up, mem_left

    lines = text_input.splitlines()
    result = 0
    greed = [[int(n) for n in line] for line in lines]
    mem_up = [0] * len(greed[0])
    mem_left = 0

    for i, line in enumerate(greed):
        for j, n in enumerate(line):
            if is_visible(greed, i, j):
                result += 1

    print(result)
    return result


mem_up = []
mem_left = 0


def is_visible(greed, i, j):
    global mem_up, mem_left

    # up
    flag = False
    if greed[i][j] > mem_up[j]:
        flag = True
    # left
    if greed[i][j] > mem_left:
        flag = True

    # update mem after check
    mem_left = max(mem_left, greed[i][j])
    if j == 0:
        mem_left = greed[i][j]
    mem_up[j] = max(mem_up[j], greed[i][j])

    if flag:
        return True

    # 0
    if i == 0 or j == 0 or i == (len(greed) - 1) or j == (len(greed[0]) - 1):
        return True

    # down
    flag = True
    for k in range(i + 1, len(greed)):
        if greed[k][j] >= greed[i][j]:
            flag = False
            break
    if flag:
        return True

    # right
    for k in range(j + 1, len(greed[0])):
        if greed[i][k] >= greed[i][j]:
            return False

    return True


##########################


def aoc_2(text_input):
    lines = text_input.splitlines()
    result = 0
    greed = [[int(n) for n in line] for line in lines]
    for i, line in enumerate(greed):
        for j, n in enumerate(line):
            s = score(greed, i, j)
            result = max(s, result)

    print(result)
    return result


def score(greed, i, j):
    if i == 0 or j == 0 or i == (len(greed) - 1) or j == (len(greed[0]) - 1):
        return 0

    curr = greed[i][j]

    left = 0
    for k in range(j - 1, -1, -1):
        left += 1
        if greed[i][k] >= curr:
            break
    right = 0
    for k in range(j + 1, len(greed[0])):
        right += 1
        if greed[i][k] >= curr:
            break

    up = 0
    for k in range(i - 1, -1, -1):
        up += 1
        if greed[k][j] >= curr:
            break
    down = 0
    for k in range(i + 1, len(greed)):
        down += 1
        if greed[k][j] >= curr:
            break

    m = left * right * up * down
    return m


assert aoc_1(e1) == 21
# aoc_1(s8)  # 1798

assert aoc_2(e1) == 8
aoc_2(s8)  # 259308
