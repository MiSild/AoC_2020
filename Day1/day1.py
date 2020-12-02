from file_helper import *

expenses = read_text_into_list()
expenses = [int(i.strip()) for i in expenses]
goal = 2020
length = len(expenses)
first_task = False

if first_task:
    for i in range(length):
        for j in range(i + 1, length):
            if expenses[i] + expenses[j] == goal:
                print(expenses[i] * expenses[j])
else:
    for i in range(length):
        if expenses[i] > goal:
            continue
        for j in range(i + 1, length):
            if expenses[i] + expenses[j] > goal:
                continue
            for k in range(j + 1, length):
                if expenses[i] + expenses[j] + expenses[k] == goal:
                    print(expenses[i] * expenses[j] * expenses[k])
