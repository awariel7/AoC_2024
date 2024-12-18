def safety_factor_calc(robots, h, w, t):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for k, v in robots.items():
        start_position = v[0]
        robot_speed = v[1]
        y = (start_position[0] + robot_speed[0] * t) % h
        x = (start_position[1] + robot_speed[1] * t) % w
        # check quadrants
        # first quadrant 0 <= x <= h // 2; 0 <= y <= w //2
        # second quadrant h // 2 + 1 <= x <= h; 0 <= y <= w //2
        # third quadrant 0 <= x <= h // 2; w //2 + 1 <= y <= w
        # forth quadrant h // 2 + 1 <= x <= h; w //2 + 1 <= y <= w

        if 0 <= y < h // 2 and 0 <= x < w // 2:
            q1 += 1
        elif h // 2 + 1 <= y < h and 0 <= x < w // 2:
            q2 += 1
        elif 0 <= y < h // 2 and w // 2 + 1 <= x < w:
            q3 += 1
        elif h // 2 + 1 <= y < h and w // 2 + 1 <= x < w:
            q4 += 1
    safety_factor = q1 * q2 * q3 * q4
    return safety_factor

with open("data.txt", "r") as file:
    robots_list = [line.strip() for line in file]

RLL = len(robots_list)

robots = {}
for n in range(RLL):
    s1 = robots_list[n]
    fp = s1.find('=') + 1
    comma = s1.find(',')
    v = s1.find('v')
    start = (int(s1[fp:comma]), int(s1[comma + 1:v].strip()))
    nv = s1[v+2:]
    s_comma = nv.find(',')
    speed = (int(nv[:s_comma]), int(nv[s_comma + 1:]))
    robots[n] = [start, speed]

print(robots)
t = 100 # 100 secs
'''
The robots outside the actual bathroom are in a space which is 101 tiles wide and 103 tiles tall 
'''
h = 101
w = 103
#test
#h = 11 #11
#w = 7 #7
tiles = [['.' for k in range(h)] for j in range(w)]

for k, v in robots.items():
    s = v[0]
    y = s[0]
    x = s[1]
    if tiles[x][y] == '.':
        tiles[x][y] = 1
    else:
        tiles[x][y] += 1
print('Start position')
for i in range(len(tiles)):
    print(*tiles[i])

tiles.clear()
tiles = [['.' for k in range(h)] for j in range(w)]


sf = safety_factor_calc(robots, h, w, t)
for k, v in robots.items():
    start_position = v[0]
    robot_speed = v[1]
    y = (start_position[0] + robot_speed[0] * t) % h
    x = (start_position[1] + robot_speed[1] * t) % w
    if tiles[x][y] == '.':
        tiles[x][y] = 1
    else:
        tiles[x][y] += 1

print('Final position')
for i in range(len(tiles)):
    print(*tiles[i])

print(f'Safety factor = {sf}')

