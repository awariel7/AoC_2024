# read file
with open("data.txt", "r") as file:
    lines = [line.rstrip() for line in file]
rules = [r for r in lines[:lines.index('')]]
pages = [[n for n in pg.split(',')] for pg in lines[lines.index('') + 1:]]
res = 0
incorrect_pages = []
for p in pages:
    c = 0
    for j in range(1, len(p)):
        ch = p[j-1] + '|' + p[j]
        rev_ch = p[j] + '|' + p[j-1]
        if ch in rules:
            if p.index(p[j]) > p.index(p[j-1]):
                c += 1
            else:
                break
        elif rev_ch in rules:
            if p.index(p[j]) < p.index(p[j-1]):
                c += 1
            else:
                break
        else:
            c += 1
    if c == len(p) - 1:
        mid = len(p)//2
        res += int(p[mid])
    else:
        # collect all the incorrect pages for part 2
        incorrect_pages.append(p)
print(f'Part 1: {res}')

res_incorrect = 0
for p in incorrect_pages:
    f_incorrect = True
    # while we won't sort seq correctly
    # is there a way to upgrade sorting?
    while f_incorrect == True:
        c = 0
        for j in range(1, len(p)):
            ch = p[j - 1] + '|' + p[j]
            rev_ch = p[j] + '|' + p[j - 1]
            if ch in rules:
                if p.index(p[j]) > p.index(p[j - 1]):
                    c += 1
                else:
                    f_incorrect = True
                    p[j - 1], p[j] = p[j], p[j - 1]
            elif rev_ch in rules:
                if p.index(p[j]) < p.index(p[j - 1]):
                    c += 1
                else:
                    f_incorrect = True
                    p[j], p[j - 1] = p[j - 1], p[j]
            else:
                c += 1
        if c == len(p) - 1:
            f_incorrect = False
    mid = len(p) // 2
    res_incorrect += int(p[mid])
print(f'Part 2: {res_incorrect}')
