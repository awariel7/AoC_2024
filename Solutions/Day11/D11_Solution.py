from functools import lru_cache

@lru_cache(None)  # Use memoization
def count_stones_optimized(stone, blink):
    if blink == 0:
        return 1

    b = blink - 1
    c = 0
    if stone == '0':
        c += count_stones_optimized('1', b)
    else:
        CL = len(stone)
        if CL % 2 == 0:
            mid = CL // 2
            s1 = str(int(stone[:mid]))
            s2 = str(int(stone[mid:]))
            c += count_stones_optimized(s1, b) + count_stones_optimized(s2, b)
        else:
            n = int(stone) * 2024
            c += count_stones_optimized(str(n), b)
    return c


with open("data.txt", "r") as file:
    s = [line.rstrip().split() for line in file]
stones = s[0]
blinks = 25
res = sum(count_stones_optimized(st, blinks) for st in stones)
print(f'Stones amount 1: {res}')

blinks_2 = 75
res_2 = 0
for i, st in enumerate(stones):
    res_2 += count_stones_optimized(st, blinks_2)
    print(f'Result after stone {st} ({i + 1}/{len(stones)}) is {res_2}')
print(f'Stones amount 2: {res_2}')
