'''

Horrible bruteforce. We can do better!
'''
data = ''
with open("data.txt", "r") as file:
    for line in file:
        data += line.rstrip()
blocks = []
spaces = []
data_info = list(data)

for i in range(0, len(data_info), 2):
    blocks.append(int(data_info[i]))
for j in range(1, len(data_info), 2):
    spaces.append(int(data_info[j]))

decompressed_data = []
dot = '.'
for i in range(len(blocks)):
    for _ in range(blocks[i]):
        decompressed_data.append(str(i))
    if i < len(spaces):
        for _ in range(spaces[i]):
            decompressed_data.append(dot)

compressed_data = []
last_index = -1
DDL = len(decompressed_data)
for di in range(DDL):
    d = decompressed_data[di]
    if d != '.':
        compressed_data.append(d)
        if last_index == di - DDL:
            break
    else:
        while decompressed_data[last_index].isdigit() is not True:
            last_index -= 1
        else:
            compressed_data.append(decompressed_data[last_index])
            last_index -= 1
res = 0
for n_index in range(len(compressed_data)):
    res += n_index * int(compressed_data[n_index])
print(f'Part 1: {res}')
# Part 2
f_data = []
file_count = len(blocks) - 1
decompressed_data.reverse()
for f in range(file_count, -1, -1):
    current_file_id = str(f)
    file_start = decompressed_data.index(current_file_id)
    nd = decompressed_data[file_start:]
    for n in range(len(nd)):
        if nd[n] != current_file_id:
            next_id = n + file_start
            break
    else:
        continue
    file_len = next_id - file_start
    dot_counter = 0
    for back_i in range(-1, -1 * DDL - 1 + file_start, -1):
        if decompressed_data[back_i] == '.':
            dot_counter += 1
        else:
            if dot_counter >= file_len:
                for k in range(file_len):
                    decompressed_data[back_i + dot_counter - k], decompressed_data[file_start + k] = \
                        decompressed_data[file_start + k], decompressed_data[back_i + dot_counter - k]
                dot_counter = 0
                break
            else:
                dot_counter = 0
decompressed_data.reverse()
res2 = 0
for n_index in range(len(decompressed_data)):
    if decompressed_data[n_index] == dot:
        continue
    else:
        res2 += n_index * int(decompressed_data[n_index])
print(f'Part 2: {res2}')








