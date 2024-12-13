# Unusable for Part 2
with open("../data.txt", "r") as file:
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

print(machines)
machines_tokens_1 = {}
machines_tokens_2 = {}

for k, v in machines.items():
    l = v
    prize_x = l[2][0]
    prize_y = l[2][1]

    buttonA_x = l[0][0]
    buttonA_y = l[0][1]
    buttonB_x = l[1][0]
    buttonB_y = l[1][1]

    start = prize_x // buttonA_x
    for i in range(start, 0, -1):
        if (prize_x - buttonA_x * i) % buttonB_x == 0:
            count_x = i
            count_y = (prize_x - buttonA_x * i) // buttonB_x
            if prize_y == buttonA_y * count_x + buttonB_y * count_y:
                machines_tokens_1[k] = (count_x, count_y)
                break
        else:
            continue

res = 0
for k, v in machines_tokens_1.items():
    print(f'Machine {k}: {v}')
    res += v[0] * price_A + v[1] * price_B

print(res)