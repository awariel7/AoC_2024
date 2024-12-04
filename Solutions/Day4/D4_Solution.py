# read file
with open("data.txt", "r") as file:
    # create matrix from symbols
    lines = [[c for c in line.rstrip()] for line in file]
# create rows from every line, column
# then we could check them with .find method forward and backward
# and I decided to work separately with diagonals
rows_and_cols = []
# word for search
word = 'XMAS'
# result counters
xmas_counter_rows_cols = 0
xmas_counter_diagonals = 0
# fill list with rows
for i in range(len(lines)):
    rows_and_cols.append(''.join(lines[i]))
# fill list with cols
for j in range(len(lines[0])):
    column = ''
    for i in range(len(lines)):
        column += lines[i][j]
    rows_and_cols.append(column)
# check diagonals
n, k = len(lines), len(lines[0])
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'X':
            # check 4 directions
            for m in range(4):
                # start position "X"
                r = i
                c = j
                check_word = 'X'
                for s in range(1, 4):
                    if m == 0:
                        r += 1
                        c += 1
                    if m == 1:
                        r -= 1
                        c += 1
                    if m == 2:
                        r -= 1
                        c -= 1
                    if m == 3:
                        r += 1
                        c -= 1
                    # if not out of the range
                    if 0 <= r < n and 0 <= c < k:
                        check_word += lines[r][c]
                if check_word == word:
                    xmas_counter_diagonals += 1

# search in rows and cols forward and backward
for r in rows_and_cols:
    nl = r
    nlr = r[::-1]
    while nl.find(word) != -1:
        c = nl.find(word)
        xmas_counter_rows_cols += 1
        nl = nl[c + 1:]
    while nlr.find(word) != -1:
        c = nlr.find(word)
        xmas_counter_rows_cols += 1
        nlr = nlr[c + 1:]
# print(f'Part1. rows and cols: {xmas_counter_rows_cols}, diagonals: {xmas_counter_diagonals}')
print(f'Part1. Total: {xmas_counter_rows_cols + xmas_counter_diagonals}')

# Part 2
x_mas_counter = 0
MAS_word_set = set('MAS')
# check diagonals
# info for check
n, k = len(lines), len(lines[0])
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'A':
            # start position "A"
            check_word1 = ''
            check_word2 = ''
            # if not out of the range
            if 0 <= i + 1 < n and 0 <= j + 1 < k and 0 <= i - 1 < n and 0 <= j - 1 < k:
                check_word1 = lines[i + 1][j - 1] + 'A' + lines[i - 1][j + 1]
                check_word2 = lines[i - 1][j - 1] + 'A' + lines[i + 1][j + 1]
                # check each set with target
                if set(check_word1) == MAS_word_set and set(check_word2) == MAS_word_set:
                    x_mas_counter += 1
print(f'Part2. Total: {x_mas_counter}')
