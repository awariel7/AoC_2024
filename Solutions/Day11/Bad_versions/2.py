def count_stones(stone, blink):
    b = blink - 1
    c = 0
    CL = len(stone)
    if blink > 0:
        if stone == '0':
            c += count_stones('1', b)
        elif CL % 2 == 0:
            s1 = str(int(stone[:CL // 2]))
            s2 = str(int(stone[CL // 2:]))
            c += count_stones(s1, b) + count_stones(s2, b)
        else:
            n = int(stone)
            n *= 2024
            c += count_stones(str(n), b)
    else:
        c += 1
    return c

with open("data.txt", "r") as file:
    s = [line.rstrip().split() for line in file]
stones = s[0]
print(stones)
blinks = 25
res = 0
for st in stones:
    res += count_stones(st, blinks)
print(f'Stones amount 1: {res}')

blinks_2 = 75
res_2 = 0
for st in stones:
    res_2 += count_stones(st, blinks_2)
    print(f'Result after stone {st} is {res_2}')
print(f'Stones amount 2: {res_2}')