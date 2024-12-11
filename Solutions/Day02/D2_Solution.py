def list_check(l):
    cur = 0
    prev = 0
    res = True
    for j in range(1, len(l)):
        if abs(l[j] - l[j - 1]) > 3 or abs(l[j] - l[j - 1]) < 1:
            res = False
            break
        prev, cur = cur, l[j] - l[j - 1]
        if (cur > 0 and prev < 0) or (cur < 0 and prev > 0):
            res = False
            break
    return res
# read file
with open("data.txt", "r") as file:
  lines = [line.rstrip() for line in file]

safe_reports = 0
d = {}
result = False
for i in range(len(lines)):
    l = [int(c) for c in lines[i].split()]
    for j in range(len(l)):
        nl = l[:j] + l[j+1:]
        # Part 1 402
        # result = list_check(l)
        # Part 2 455
        result = list_check(nl)
        if result:
            safe_reports += 1
            break
    d[i] = (l, result)

print(safe_reports)
# print(d)