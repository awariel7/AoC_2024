import numpy as np

with open("data.txt", "r") as file:
    machine_list = [line for line in file]

MLL = len(machine_list)
price_A = 3
price_B = 1
mil = 10000000000000
machines = {}
for n in range(0, MLL, 4):
    s1 = machine_list[n]
    fp = s1.find('+') + 1
    comma = s1.find(',')
    buttonA = (int(s1[fp:comma]), int(s1[comma + 4:]))
    s2 = machine_list[n + 1]
    fp = s2.find('+') + 1
    comma = s2.find(',')
    buttonB = (int(s2[fp:comma]), int(s2[comma + 4:]))
    s3 = machine_list[n + 2]
    fp = s3.find('=') + 1
    comma = s3.find(',')
    prize1 = (int(s3[fp:comma]), int(s3[comma + 4:]))
    prize2 = (int(s3[fp:comma]) + mil, int(s3[comma + 4:]) + mil)
    machines[n] = [buttonA, buttonB, prize1, prize2]

machines_tokens_1 = {}
machines_tokens_2 = {}

for k, v in machines.items():
    l = v
    A = np.array([
        [l[0][0], l[1][0]],
        [l[0][1], l[1][1]]
    ])
    B1 = np.array([l[2][0], l[2][1]])
    B2 = np.array([l[3][0], l[3][1]])

    solution1 = np.linalg.solve(A, B1)
    x, y = solution1
    if round(float(x), 2) % 1 == 0.00 and round(float(y), 2) % 1 == 0.00:
        machines_tokens_1[k] = (int(round(float(x) + 0.00000000001, 2)), int(round(float(y) + 0.00000000001, 2)))


    solution2 = np.linalg.solve(A, B2)
    x, y = solution2
    if round(float(x), 2) % 1 == 0.00 and round(float(y), 2) % 1 == 0.00:
        machines_tokens_2[k] = (round(float(x) + 0.000000000001, 0), round(float(y) + 0.000000000001, 0))

res_1 = 0
for k, v in machines_tokens_1.items():
    # print(f'Machine {k}: {v}')
    res_1 += v[0] * price_A + v[1] * price_B
print(f'Part 1. Total tokens to pay: {res_1}')

res_2 = 0
for v in machines_tokens_2.values():
    res_2 += v[0] * price_A + v[1] * price_B
print(f'Part 2. Total tokens to pay: {res_2}')
