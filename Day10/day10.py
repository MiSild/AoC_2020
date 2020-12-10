from file_helper import *
import copy

max_diff = 3

rows = [int(row.strip()) for row in read_text_into_list()]
rows.sort()
rows.insert(0, 0)
single = 0
triple = 1

for i in range(1, len(rows)):
    if rows[i] - rows[i-1] == 1:
        single += 1
    elif rows[i] - rows[i-1] == 3:
        triple += 1

print(single * triple)
"""rows = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]"""

unique_arrangements = 0
uniques = {len(rows) - 1: 1}


def get_reachables(index):
    global uniques
    reachables = 0
    for i in range(index + 1, len(rows)):
        if rows[i] - rows[index] <= 3:
            reachables += uniques[i]
        else:
            break
    uniques[index] = reachables


for i in range(len(rows) - 2, -1, -1):
    get_reachables(i)

print(uniques[0])