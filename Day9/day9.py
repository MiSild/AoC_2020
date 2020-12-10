from file_helper import *
from collections import deque

rows = [int(row.strip()) for row in read_text_into_list()]

preamble_length = 25
last_numbers = deque()
invalid_number = 0

def valid_number(number, number_deque):
    for j in number_deque:
        for k in number_deque:
            if j + k == number:
                return True
    return False

for i in range(len(rows)):
    if i < preamble_length:
        last_numbers.appendleft(rows[i])
    elif valid_number(rows[i], last_numbers):
        last_numbers.appendleft(rows[i])
        last_numbers.pop()
    else:
        print(rows[i])
        invalid_number = rows[i]
        break
should_break = False
for i in range(len(rows)):
    invalid_set = []
    current_sum = 0
    for k in range(i, len(rows)):
        if current_sum > invalid_number:
            break
        elif current_sum == invalid_number:
            should_break = True
            break
        current_sum += rows[k]
        invalid_set.append(rows[k])

    if should_break:
        break

print(min(invalid_set) + max(invalid_set))

