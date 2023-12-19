from aoc19.aoc_input import s1

e1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


def aoc_1(text_input):
    w, r = text_input.split("\n\n")
    workflows = w.splitlines()
    ratings = r.splitlines()

    accepted = []
    workflow_d = get_workflows(workflows)

    for r_line in ratings:
        r_line = r_line[1:-1]
        r_line = r_line.split(",")
        r_line = [r.split("=") for r in r_line]
        rating_d = {k: int(v) for k, v in r_line}

        passed = check(rating_d, workflow_d)
        if passed:
            accepted.append(rating_d)

    result = 0
    for a in accepted:
        vs = [v for k, v in a.items() if k in "xmsa"]
        result += sum(vs)

    print(result)
    return result


def get_workflows(workflows):
    workflow_d = {}
    for w in workflows:
        name, rules = w[:-1].split("{")
        rules = rules.split(",")
        workflow_d[name] = rules
    return workflow_d


def check(rating_d, w_d):
    w = "in"
    while w not in "RA":
        tests = w_d[w]
        for t in tests:
            t = t.split(":")
            if len(t) == 1:
                w = t[0]
                break
            elif eval(t[0], rating_d):
                w = t[1]
                break
    return w == "A"


########

def aoc_2(text_input):
    w, _ = text_input.split("\n\n")
    workflows = w.splitlines()
    workflow_d = get_workflows(workflows)
    w = "in"
    curr = []
    all_paths = []
    find(all_paths, curr, w, workflow_d)

    all_paths = [a[:-1] for a in all_paths if a[-1] == "A"]
    result = 0
    # print(all_)

    for a in all_paths:
        result += count_combinations(a)
    print(result)
    return result


def count_combinations(a):
    d = {k: [1, 4001] for k in "xmsa"}  # [inclusive, exclusive]
    for i, exp in enumerate(a):

        if "<" in exp:
            k = exp.split("<")[0]
            if "=" in exp:
                num = int(exp.split("=")[1]) + 1
            else:
                num = int(exp.split("<")[1])
            d[k][1] = min(d[k][1], num)
        else:
            k = exp.split(">")[0]
            if "=" in exp:
                num = int(exp.split("=")[1])
            else:
                num = int(exp.split(">")[1]) + 1
            d[k][0] = max(d[k][0], num)

    result = 1
    for k, v in d.items():
        e = (v[1] - v[0])
        result *= e
    return result


def find(all_paths, curr, w, workflow_d):
    if w in "RA":
        curr = curr.copy()
        curr.append(w)
        all_paths.append(curr)
        return

    tests = workflow_d[w]
    curr = curr.copy()
    for t in tests:
        t = t.split(":")

        if len(t) == 1:
            w = t[0]
            curr_ = curr.copy()
            find(all_paths, curr_, w, workflow_d)
        else:
            curr_ = curr.copy()
            w = t[1]
            not_ = t[0].replace(">", "<=") if ">" in t[0] else t[0].replace("<", ">=")
            curr.append(not_)
            curr_.append(t[0])
            find(all_paths, curr_, w, workflow_d)


# assert aoc_1(e1) == 19114
# aoc_1(s1)  # 418498

assert aoc_2(e1) == 167409079868000
aoc_2(s1)  # 123331556462603
