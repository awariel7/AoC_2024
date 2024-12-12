import numpy as np
from scipy.ndimage import binary_dilation, label

with open("data.txt", "r") as file:
    map = [[l for l in line.rstrip()] for line in file]

print(map)
sym_dict = {}
sym_set = set()
directions_dict = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

R = len(map)
C = len(map[0])


for r in range(R):
    for c in range(C):
        sym_set.add(map[r][c])
# Матрица
matrix = np.array(map)
res = 0
# Символ для анализа
for s in sym_set:
    target = s
    # Маска для символа
    mask = (matrix == target)
    # Размечаем связные компоненты
    labeled_array, num_features = label(mask)
    region_map = [[r for r in row] for row in labeled_array.tolist()]
    # Инициализируем периметр
    total_perimeter = 0

    # Рассчитываем периметр для каждой области
    for region_id in range(1, num_features + 1):
        el_c = 0
        p = 0
        for r in range(R):
            for c in range(C):
                el = region_map[r][c]
                if el == region_id:
                    el_c += 1
                    for v in directions_dict.values():
                        if 0 <= r + v[0] < R and 0 <= c + v[1] < C:
                            neighbor = region_map[r + v[0]][c + v[1]]
                            if neighbor != el:
                                p += 1
                        else:
                            p += 1
        res += el_c * p
        print(f'Res for {s} is {el_c * p}')

print(f'Part 1: {res}')

