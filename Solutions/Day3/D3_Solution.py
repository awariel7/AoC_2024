# read file
# TODO: Read as a whole string
with open("data.txt", "r") as file:
  lines = [line for line in file]
l = ''
for i in lines:
    l += i
# array of mul pairs
ls = []
# first appearance
t = l.find('mul(')
# second appearance
t_next = l[t + 3:].find('mul(') + t + 3
# Enable|disable flags for Part 2
flag_do = True
flag_dont = False
while t != -1:
    if flag_do:
        ls.append(l[t:t + 12])
    # Check do() and don't() for Part 2
    # w\o them will be result for Part 1
    if l[t:t_next].find("don't()") != -1:
        flag_dont = True
        flag_do = False
    elif l[t:t_next].find("do()") != -1:
        flag_do = True
        flag_dont = False
    # not to skip short sequences
    l = l[t + 3:]
    t = l.find('mul(')
    t_next = l[t + 3:].find('mul(') + t + 3
# TODO: Is it possible not to check every symbol?
res = 0
for i in ls:
    comma = 0
    n1 = ''
    n2 = ''
    close_bracket = False
    for j in i:
        if j.isdigit() and comma == 0:
            n1 += j
        elif j.isdigit() and comma == 1:
            n2 += j
        elif j == ',':
            comma += 1
        elif j == ')':
            close_bracket = True
            break
        else:
            continue
    if n1 != '' and n2 != '' and close_bracket:
        res += int(n1) * int(n2)
print(res)