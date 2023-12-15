from dataclasses import dataclass

from aoc2022.aoc_input import s7

e1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

""" directories with a total size of at most 100000"""


@dataclass
class File:
    name: str
    size: int


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def __repr__(self):
        return f"Dir({self.name})"

    def add_dir(self, dir_):
        self.dirs.append(dir_)

    def add_file(self, name, size):
        self.files.append(File(name, size))

    def get_size(self):
        dirs_s = sum([dir_.get_size() for dir_ in self.dirs])
        files_s = sum([f.size for f in self.files])
        size = dirs_s + files_s
        return size


root = Dir("/")


def aoc_1(text_input):
    init(text_input)
    result = walk(root)

    print(result)
    return result


def init(text_input):
    global root
    root = Dir("/")
    cmds = get_cmds(text_input)
    curr_dir = root
    for cmd in cmds:
        if cmd[0].startswith("cd"):  # ['cd /']
            curr_dir = cd(cmd, curr_dir)

        elif cmd[0].startswith("ls"):  # ['ls', 'dir a', '14848514 b.txt']
            ls(cmd, curr_dir)


def walk(dir_):
    result = 0

    for d in dir_.dirs:
        s = d.get_size()
        if s <= 100_000:
            # print(d, s)
            result += s
        result += walk(d)
    return result


def ls(cmd, curr_dir):
    for item in cmd[1:]:
        if item.startswith("dir"):
            dir_name = item[4:]
            dir_ = Dir(dir_name, curr_dir)
            curr_dir.add_dir(dir_)
        else:
            size, name = item.split()
            curr_dir.add_file(name, int(size))


def cd(cmd, curr_dir):
    cmd = cmd[0]
    dir_name = cmd[3:]
    if dir_name == "..":
        curr_dir = curr_dir.parent
    elif dir_name == "/":
        curr_dir = root
    else:
        dir_ = Dir(dir_name, curr_dir)
        curr_dir.add_dir(dir_)
        curr_dir = dir_
    return curr_dir


def get_cmds(text_input):
    lines = text_input.split("\n$ ")
    cmds = []
    for cmd in lines:
        cmd_lines = cmd.splitlines()
        cmd_lines = [line.strip() for line in cmd_lines]
        cmds.append(cmd_lines)
    return cmds


############

def aoc_2(text_input):
    init(text_input)
    total = root.get_size()
    required = 30000000 - (70000000 - total)

    result = walk2(root, required)
    assert result >= required
    print(result)
    return result


def walk2(dir_, required):
    s = dir_.get_size()
    if s <= required:
        return -1
    result = s

    for d in dir_.dirs:
        r = walk2(d, required)
        if r == -1:
            continue
        result = min(result, r)
    return result


assert aoc_1(e1) == 95437
assert aoc_1(s7) == 1391690

assert aoc_2(e1) == 24933642
aoc_2(s7)  # 5469168
