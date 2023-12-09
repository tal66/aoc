from aoc02.aoc_input import s1, s2

e1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

bag = {"red": 12, "green": 13, "blue": 14}


def aoc2_1(bag, e1):
    result = 0
    for line in e1.split("\n"):
        game = line.split(":")[1].strip()
        game_id = line.split(":")[0].replace("Game ", "")
        is_possible = True
        for item in game.split(";"):
            record = to_record(item)
            for color in record:
                if bag[color] < record[color]:
                    is_possible = False
                    print(f"Game {game_id}  impossible. {color} {bag[color]} < {record[color]}")
                    break
            if not is_possible:
                break
            # print(record)

        if is_possible:
            print(f"Game {game_id}  possible")
            result += int(game_id)

    print(result)
    return result


def aoc2_2(bag, e1):
    result = 0
    lines = e1.split("\n")
    for line in lines:
        game = line.split(":")[1].strip()
        game_id = line.split(":")[0].replace("Game ", "")
        d = {}
        for item in game.split(";"):
            record = to_record(item)
            for color in record:
                if color not in d:
                    d[color] = record[color]
                    continue

                d[color] = max(d[color], record[color])

        m = 1
        for color in d:
            m *= d[color]

        print(f"Game {game_id} {d} {m}")
        result += m

    print(result)
    return result


def to_record(item: str) -> dict:
    result = {}
    for i in item.split(","):
        color_item = i.strip().split(" ")
        result[color_item[1]] = int(color_item[0])
    return result


assert aoc2_1(bag, e1) == 8
assert aoc2_1(bag, s1) == 2149
assert aoc2_2(bag, e1) == 2286
assert aoc2_2(bag, s1) == 71274
