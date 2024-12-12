with open("data.txt", "r") as file:
    s = [line.rstrip().split() for line in file]
stones = s[0]
print(stones)
blinks = 25

for _ in range(blinks):
    i = 0
    L = len(stones)
    while i < L:
        CL = len(stones[i])
        if stones[i] == '0':
            stones[i] = '1'
        elif CL % 2 == 0:
            t = stones.pop(i)
            h = str(int(t[:CL//2]))
            t = str(int(t[CL//2:]))
            stones.insert(i, h)
            stones.insert(i + 1, t)
            if i < L - 1:
                L += 1
                i += 1
        else:
            n = int(stones[i])
            n *= 2024
            stones[i] = str(n)
        i += 1
    # print(stones)
# 25
print(f'Part 1: {len(stones)}')