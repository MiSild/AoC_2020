from file_helper import *
import copy

rows = [list(row.strip()) for row in read_text_into_list()]
og_rows = copy.deepcopy(rows)

def count_neighbours(row, column, floor_plan):
    neighbours = 0
    try:
        if floor_plan[row][column + 1] == "#":
            neighbours += 1
    except IndexError:
        pass
    try:
        if floor_plan[row + 1][column + 1] == "#":
            neighbours += 1
    except IndexError:
        pass
    try:
        if floor_plan[row + 1][column] == "#":
            neighbours += 1
    except IndexError:
        pass
    try:
        if floor_plan[row - 1][column + 1] == "#" and row - 1 >= 0:
            neighbours += 1
    except IndexError:
        pass
    try:
        if floor_plan[row - 1][column] == "#" and row - 1 >= 0:
            neighbours += 1
    except IndexError:
        pass
    try:
        if floor_plan[row - 1][column - 1] == "#" and row - 1 >= 0 and column - 1 >= 0:
            neighbours += 1
    except IndexError:
        pass
    try:
        if floor_plan[row + 1][column - 1] == "#" and column - 1 >= 0:
            neighbours += 1
    except IndexError:
        pass
    try:
        if floor_plan[row][column - 1] == "#" and column - 1 >= 0:
            neighbours += 1
    except IndexError:
        pass

    return neighbours


did_change = True

while did_change:
    did_change = False
    floor = copy.deepcopy(rows)
    for row in range(len(rows)):
        for column in range(len(rows[0])):
            if count_neighbours(row, column, floor) == 0 and floor[row][column] == "L":
                rows[row][column] = "#"
                did_change = True
            elif count_neighbours(row, column, floor) >= 4 and floor[row][column] == "#":
                rows[row][column] = "L"
                did_change = True

count = 0

for row in range(len(rows)):
    for column in range(len(rows[0])):
        if rows[row][column] == "#":
            count += 1

print(count)


def count_neighbours_vision(row, column, floor_plan):
    neighbours = 0
    try:
        increase = 1
        while True:
            seen_seat = floor_plan[row][column + increase]
            if seen_seat == "#":
                neighbours += 1
                break
            elif seen_seat == "L":
                break
            increase += 1
    except IndexError:
        pass
    try:
        increase = 1
        while True:
            if floor_plan[row + increase][column + increase] == "#":
                neighbours += 1
                break
            elif floor_plan[row + increase][column + increase] == "L":
                break
            increase += 1
    except IndexError:
        pass
    try:
        increase = 1
        while True:
            if floor_plan[row + increase][column] == "#":
                neighbours += 1
                break
            elif floor_plan[row + increase][column] == "L":
                break
            increase += 1
    except IndexError:
        pass
    try:
        increase = 1
        while True:
            if floor_plan[row - increase][column + increase] == "#" and row - increase >= 0:
                neighbours += 1
                break
            elif row - increase < 0:
                break
            elif floor_plan[row - increase][column + increase] == "L":
                break
            increase += 1

    except IndexError:
        pass
    try:
        increase = 1
        while True:
            if floor_plan[row - increase][column] == "#" and row - increase >= 0:
                neighbours += 1
                break
            elif row - increase < 0:
                break
            elif floor_plan[row - increase][column] == "L":
                break
            increase += 1
    except IndexError:
        pass
    try:
        increase = 1
        while True:
            if floor_plan[row - increase][column - increase] == "#" and row - increase >= 0 and column - increase >= 0:
                neighbours += 1
                break
            elif row - increase < 0 or column - increase < 0:
                break
            elif floor_plan[row - increase][column - increase] == "L":
                break
            increase += 1
    except IndexError:
        pass
    try:
        increase = 1
        while True:
            if floor_plan[row + increase][column - increase] == "#" and column - increase >= 0:
                neighbours += 1
                break
            elif column - increase < 0:
                break
            elif floor_plan[row + increase][column - increase] == "L":
                break
            increase += 1
    except IndexError:
        pass
    try:
        increase = 1
        while True:
            if floor_plan[row][column - increase] == "#" and column - increase >= 0:
                neighbours += 1
                break
            elif column - increase < 0:
                break
            elif floor_plan[row][column - increase] == "L":
                break
            increase += 1
    except IndexError:
        pass

    return neighbours

did_change = True
rows = copy.deepcopy(og_rows)

while did_change:
    did_change = False
    floor = copy.deepcopy(rows)
    for row in range(len(rows)):
        for column in range(len(rows[0])):
            if count_neighbours_vision(row, column, floor) == 0 and floor[row][column] == "L":
                rows[row][column] = "#"
                did_change = True
            elif count_neighbours_vision(row, column, floor) >= 5 and floor[row][column] == "#":
                rows[row][column] = "L"
                did_change = True

count = 0

for row in range(len(rows)):
    for column in range(len(rows[0])):
        if rows[row][column] == "#":
            count += 1

print(count)