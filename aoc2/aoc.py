from aoc2.aoc_input import s1, s2


e1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

bag = {"red": 12, "green": 13, "blue": 14}

def aoc2_1(bag, e1):
    result = 0
    for line in e1.split("\n"):
        # print(line)
        game = line.split(":")[1].strip()
        game_id = line.split(":")[0].replace("Game ", "")
        is_possible = True
        for item in game.split(";"):
            revealed = to_record(item)
            for color in revealed:
                if bag[color] < revealed[color]:
                    is_possible = False
                    print(f"Game {game_id}  impossible. {color} {bag[color]} < {revealed[color]}")
                    break
            if not is_possible:
                break
            # print(revealed)

        if is_possible:
            print(f"Game {game_id}  possible")
            result += int(game_id)



    print(result)
    return result

def aoc2_2(bag, e1):
    result = 0
    for line in e1.split("\n"):
        # print(line)
        game = line.split(":")[1].strip()
        game_id = line.split(":")[0].replace("Game ", "")
        d = {}
        for item in game.split(";"):
            revealed = to_record(item)
            for color in revealed:
                if color in d:
                    d[color] = max(d[color], revealed[color])
                else:
                    d[color] = revealed[color]

        m = 1
        for color in d:
            m *= d[color]

        print(f"Game {game_id} {d} {m}")
        result += m



    print(result)
    return result

def to_record(item: str):
    result = {}
    for i in item.split(","):
        color_item = i.strip().split(" ")
        result[color_item[1]] = int(color_item[0])
    return result


# aoc2_1(bag, e1) # 8
# aoc2_1(bag, s1) # 2149
# aoc2_2(bag, e1) # 2286
# aoc2_2(bag, s1) # 71274
