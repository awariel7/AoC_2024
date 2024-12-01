# read file
with open("data.txt", "r") as file:
  lines = [line.rstrip() for line in file]
# lists
left_list = []
right_list = []
# fill lists
for i in lines:
    st = i.split()
    left_list.append(int(st[0]))
    right_list.append(int(st[1]))
# sort lists for correct comparison
left_list.sort()
right_list.sort()
# Calc res for Part 1
# 11651298
res = 0
for i in range(len(left_list)):
    res += abs(left_list[i] - right_list[i])
print(res)
# Calc res for Part 2
# 21306195
res2 = 0
for i in range(len(left_list)):
    res2 += left_list[i] * right_list.count(left_list[i])
print(res2)