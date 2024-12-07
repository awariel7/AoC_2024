import itertools
d = {}
# read file
with open("data.txt", "r") as file:
    lines = [line.rstrip() for line in file]

for l in lines:
    r = int(l[:l.index(':')])
    eq = [int(k) for k in l[l.index(':') + 1 :].split()]
    d[r] = eq
operators = ['*', '+']
new_operators = ['*', '+', '||']
possible_operators = []
new_possible_operators = []
res = 0
total_calibration_result = 0
total_calibration_result_2 = 0
for k, v in d.items():
    possible_operators.clear()
    new_possible_operators.clear()
    o = len(v) - 1
    possible_combinations = 2 ** o
    # Part 1
    possible_operators = list(itertools.product(operators, repeat=o))
    # Part 2
    new_possible_operators = list(itertools.product(new_operators, repeat=o))
    for po in possible_operators:
        for i in range(1, len(v)):
            if i == 1:
                if po[i - 1] == '*':
                    res = v[i-1] * v[i]
                elif po[i - 1] == '+':
                    res = v[i - 1] + v[i]
            else:
                if po[i - 1] == '*':
                    res *= v[i]
                elif po[i - 1] == '+':
                    res += v[i]
        if res == k:
            total_calibration_result += res
            break
    for npo in new_possible_operators:
        for i in range(1, len(v)):
            if i == 1:
                if npo[i - 1] == '*':
                    res = v[i-1] * v[i]
                elif npo[i - 1] == '+':
                    res = v[i - 1] + v[i]
                elif npo[i - 1] == '||':
                    res = int(str(v[i - 1]) + str(v[i]))
            else:
                if npo[i - 1] == '*':
                    res *= v[i]
                elif npo[i - 1] == '+':
                    res += v[i]
                elif npo[i - 1] == '||':
                    res = int(str(res) + str(v[i]))
        if res == k:
            total_calibration_result_2 += res
            break
# 5512534574980 O_o
print(total_calibration_result)
# 328790210468594
print(total_calibration_result_2)
