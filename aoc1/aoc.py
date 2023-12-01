from aoc1.aoc_input import s, s1

def aoc1_1(s: str) -> int:
    sum = 0
    for line in s.split("\n"):
        left = 0
        right = len(line) - 1
        while (left < right):
            flag = 0
            if line[left].isdigit():
                flag += 1
            else:
                left += 1

            if line[right].isdigit():
                flag += 1
            else:
                right -= 1

            if flag >= 2:
                break
        n = line[left] + line[right]
        print(f"{n} {line}")
        sum += int(n)
    return sum


valid_digits: dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}


def aoc1_2(s: str) -> int:
    sum = 0
    for line in s.split("\n"):
        left = 0
        right = len(line) - 1
        left_word = ""
        right_word = ""
        left_num = 0
        right_num = 0
        left_flag = False
        right_flag = False
        
        while (left <= right):

            if not left_flag:
                if line[left].isdigit():
                    left_num = int(line[left])
                    left_flag = True
                else:
                    left_word += line[left]
                    n = from_dict(left_word, "left")
                    if n != -1:
                        left_num = n
                        left_flag = True
                    else:
                        left += 1

            if not right_flag:
                if line[right].isdigit():
                    right_num = int(line[right])
                    right_flag = True
                else:
                    right_word = line[right] + right_word
                    n = from_dict(right_word, "right")
                    if n != -1:
                        right_num = n
                        right_flag = True
                    else:
                        right -= 1

            if left_flag and right_flag:
                break

        if left_num == 0:
            left_num = right_num
        elif right_num == 0:
            right_num = left_num
        # print(f"{left_num} {right_num}")
        n = left_num*10 + right_num
        print(f"{n} {line}")
        sum += int(n)
    return sum

def from_dict(s: str, left_or_right) -> int:
    for i in range(len(s)):
        if left_or_right == "left":
            sub = s[i:len(s)]
        else:
            sub = s[0:len(s)-i]

        # print(f"check {sub}")
        if sub in valid_digits:
            # print(f"return {sub} {valid_digits[sub]}")
            return valid_digits[sub]
    return -1


print(aoc1_2(s)) # 54208

# print(aoc1_1(s)) # 54940

def testing():
    assert aoc1_2("15nine1") == 11
    assert aoc1_2("7877pzrbtcsddmrffzdsmqlqkjsix") == 76
    assert aoc1_2("5four3eight") == 58
    assert aoc1_2("fourhzgxqtxggfpprrmtfqsdhc2fdxnjdgx64five") == 45
    assert aoc1_2("threeninejdzzrbpmfhjcqdsix8two2bb") == 32
    assert aoc1_2("97gldxj") == 97
    assert aoc1_2("75kp") == 75
    assert aoc1_2("114") == 14
    assert aoc1_2("1148pdtcl1eight5oneights") == 18
    assert aoc1_2("5fivekxfzpzjsd42sevenzgfourtwo") == 52
    assert aoc1_2("5dncccmkpqtwocmmlltvbg") == 52
    assert aoc1_2("dbmxvpsvp7jdnvsdnlv") == 77

# testing()