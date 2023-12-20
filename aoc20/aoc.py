from collections import deque

from aoc20.aoc_input import s1

e1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

e2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


def aoc_1(text_input):
    d = build(text_input)

    n_times = 1000
    counters = {"low": n_times, "high": 0}
    for j in range(n_times):
        click(j, d, counters=counters)

    print(counters)
    result = counters["low"] * counters["high"]
    print(result)
    return result


def click(j, d, counters=None, senders=()):
    q = deque()
    q.append("broadcaster")
    i = 0
    while q and i < 10 ** 5:
        name = q.popleft()
        prop = d[name]
        pulse = prop["pulse"]

        if prop["type"] == "&":
            inputs_pulse = [v == "high" for v in prop["inputs"].values()]
            pulse = "low" if all(inputs_pulse) else "high"

        if name in senders and pulse == "high":
            senders[name].append(j)

        for rcvr_name in prop["to"]:
            if counters:
                counters[pulse] += 1

            rcvr_prop = d[rcvr_name]
            if rcvr_prop["type"] == "&":
                rcvr_prop["inputs"][name] = pulse
            elif rcvr_prop["type"] == "%" and pulse == "low":
                rcvr_prop["pulse"] = "low" if rcvr_prop["pulse"] == "high" else "high"
            else:  # ignore "%" && "high"
                continue

            q.append(rcvr_name)
        i += 1


def build(text_input):
    d = {}
    for line in text_input.split("\n"):
        name, to_ = line.split(" -> ")

        if name[0] in "&%":
            type_, name = name[0], name[1:]
        else:
            type_ = name

        d[name] = {"to": to_.split(", "), "type": type_, "pulse": "low", "inputs": {}}

    # update missing and inputs
    to_append = {}
    for k, v in d.items():
        for rcvr_name in v["to"]:
            if rcvr_name not in d:
                to_append[rcvr_name] = {"to": [], "type": "%", "pulse": "low", "inputs": {}}
            elif d[rcvr_name]["type"] == "&":
                d[rcvr_name]["inputs"][k] = "low"
    d.update(to_append)

    return d


""" 
&nc -> rx
"""


def get_senders(d, name):
    return [k for k, v in d.items() if name in v["to"]]


def aoc_2(text_input):
    d = build(text_input)

    rx_sender_x1 = get_senders(d, "rx")[0]
    rx_sender_x2 = get_senders(d, rx_sender_x1)
    senders_d = {k: [] for k in rx_sender_x2}

    n_times = 10 ** 5
    for j in range(1, n_times):
        click(j, d, senders=senders_d)

        if all(senders_d.values()):
            break

    print(senders_d)
    result = 1
    for k, v in senders_d.items():  # lcm more correct, but they're primes in my case
        result *= v[0]

    print(result)
    return result


assert aoc_1(e1) == 32000000  # 8000 low * 4000 high
assert aoc_1(e2) == 11687500  # 4250 low * 2750 high
aoc_1(s1)  # 1020211150

aoc_2(s1)  # 238815727638557
