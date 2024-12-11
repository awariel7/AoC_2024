def trail_seek(r, c, current_head, start_x, start_y):
    if 0 <= r < R and 0 <= c < C:
        if map[r][c] == current_head + 1:
            if map[r][c] == 9:
                height_pos = (r, c)
                trails_dict[start_x, start_y] += 1
                return height_pos
            else:
                ch = map[r][c]
                for v in directions_dict.values():
                    h_pos = trail_seek(r + v[0], c + v[1], ch, start_x, start_y)
                    if h_pos is not None:
                        height_set.add(h_pos)
    else:
        return None

with open("data.txt", "r") as file:
    map = [[int(l) for l in line.rstrip()] for line in file]
R = len(map)
C = len(map[0])
trailheads_dict = {}
trails_dict = {}
directions_dict = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
height_set = set()
for i in range(R):
    for j in range(C):
        if map[i][j] == 0:
            height_set.clear()
            current_head = map[i][j]
            trails_dict[(i, j)] = 0
            for v in directions_dict.values():
                h_pos = trail_seek(i + v[0], j + v[1], current_head, i, j)
                if h_pos is not None:
                    height_set.add(h_pos)
            trailheads_dict[(i, j)] = list(height_set)

res = 0
res2 = 0
for k, v in trailheads_dict.items():
    res += len(v)
print(f'Part 1: {res}')

for k, v in trails_dict.items():
    res2 += v
print(f'Part 2: {res2}')