import re

from aoc06.aoc_input import s1, s2

e1 = """Time:      7  15   30
Distance:  9  40  200"""

# number of ways you can beat the record in each race

def aoc_1(text_input):
    lines = text_input.split('\n')

    times = re.split(r":\s+", lines[0])[1]
    times = re.split(r"\s+", times)

    distances = re.split(r":\s+", lines[1])[1]
    distances = re.split(r"\s+", distances)

    times = [int(t) for t in times]
    distances = [int(d) for d in distances]

    results = [0 for _ in range(len(times))]
    for i in range(len(times)):
        time = times[i]
        for t in range(time):
            hold = t
            d = (time-hold)*hold
            if d > distances[i]:
                results[i] += 1

    print(results)
    m = results[0]
    for i in range(1, len(results)):
        m *= results[i]
    print(m)

def aoc_2(text_input):
    lines = text_input.split('\n')
    times = re.split(r":\s+", lines[0])[1]
    times = re.split(r"\s+", times)
    time = ""
    for i in range(len(times)):
        time += times[i]
    time = int(time)

    distances = re.split(r":\s+", lines[1])[1]
    distances = re.split(r"\s+", distances)
    distance = ""
    for i in range(len(distances)):
        distance += distances[i]
    distance = int(distance)

    print(time, distance)
    result = 0
    flag = False
    for t in range(1, time):
        hold = t
        d = (time-hold)*hold
        if d > distance:
            result += 1
            flag = True
        if flag and d < distance:
            break
    print(result)

# aoc_1(e1) # 288
# aoc_1(s1)  # 131376


# aoc_2(e1) # 71503
aoc_2(s1) # 34123437
# TODO: change to binary search
