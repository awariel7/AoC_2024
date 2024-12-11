def path_finder(cur_pos_x, cur_pos_y):
    flag_continue = True
    # up
    if map[cur_pos_x][cur_pos_y] == '^':
        # check move up
        if cur_pos_x - 1 > -1:
            # if we face an obstacle then turn right
            if map[cur_pos_x - 1][cur_pos_y] == '#':
                map[cur_pos_x][cur_pos_y] = '>'
            # else move up
            else:
                map[cur_pos_x][cur_pos_y] = 'X'
                cur_pos_x -= 1
                map[cur_pos_x][cur_pos_y] = '^'
        # id we can't move up - exit
        else:
            flag_continue = False
    # right
    elif map[cur_pos_x][cur_pos_y] == '>':
        # check move right
        if cur_pos_y + 1 < len(map[0]):
            # if we face an obstacle then turn down
            if map[cur_pos_x][cur_pos_y + 1] == '#':
                map[cur_pos_x][cur_pos_y] = 'v'
            # else move right
            else:
                map[cur_pos_x][cur_pos_y] = 'X'
                cur_pos_y += 1
                map[cur_pos_x][cur_pos_y] = '>'
        # id we can't move right - exit
        else:
            flag_continue = False
    # down
    elif map[cur_pos_x][cur_pos_y] == 'v':
        # check move down
        if cur_pos_x + 1 < len(map):
            # if we face an obstacle then turn left
            if map[cur_pos_x + 1][cur_pos_y] == '#':
                map[cur_pos_x][cur_pos_y] = '<'
            # else move down
            else:
                map[cur_pos_x][cur_pos_y] = 'X'
                cur_pos_x += 1
                map[cur_pos_x][cur_pos_y] = 'v'
        # id we can't move down - exit
        else:
            flag_continue = False
    # left
    elif map[cur_pos_x][cur_pos_y] == '<':
        # check move left
        if cur_pos_y - 1 > -1:
            # if we face an obstacle then turn up
            if map[cur_pos_x][cur_pos_y - 1] == '#':
                map[cur_pos_x][cur_pos_y] = '^'
            # else move left
            else:
                map[cur_pos_x][cur_pos_y] = 'X'
                cur_pos_y -= 1
                map[cur_pos_x][cur_pos_y] = '<'
        # id we can't move left - exit
        else:
            flag_continue = False
    return cur_pos_x, cur_pos_y, flag_continue

# read file
with open("test.txt", "r") as file:
    map = [[l for l in line.rstrip()] for line in file]
# guard position
cur_pos_x = 0
cur_pos_y = 0
# path set
path_set = set()
# path set w directions
path_set_dir = set()
possible_loop_counter = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '^':
            cur_pos_x = i
            cur_pos_y = j
            break
print(cur_pos_x, cur_pos_y)
flag_continue = True
p_x, p_y = 0, 0
while flag_continue:
    if (cur_pos_x, cur_pos_y) in path_set and (p_x, p_y) != (cur_pos_x, cur_pos_y):
        possible_loop_counter += 1
    p_x, p_y = cur_pos_x, cur_pos_y
    path_set.add((cur_pos_x, cur_pos_y))
    cur_pos_x, cur_pos_y, flag_continue = path_finder(cur_pos_x, cur_pos_y)

# check final map
for m in map:
    print(*m)
print(len(path_set))
# Part 2
print(possible_loop_counter)
print(path_set_dir)

