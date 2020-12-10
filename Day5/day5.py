from file_helper import *

boarding_passes = [row.strip() for row in read_text_into_list()]
# boarding_passes = ["FBFBBFFRLR"]
rows = 127
columns = 7

highest_id = -1
seen_ids = []
for b_pass in boarding_passes:
    lower_range = 0
    higher_range = rows
    for i in range(7):
        # print(f"Lower range: {lower_range}, higher range: {higher_range}")
        if b_pass[i] == "F":
            higher_range = int((higher_range - lower_range) / 2) + lower_range
        else:
            lower_range = int((higher_range - lower_range + 1) / 2) + lower_range
    # print(f"Lower range: {lower_range}, higher range: {higher_range}")
    row = higher_range
    lower_range = 0
    higher_range = columns
    for i in range(7, 10):
        if b_pass[i] == "L":
            higher_range = int((higher_range - lower_range) / 2) + lower_range
        else:
            lower_range = int((higher_range - lower_range) / 2) + lower_range
    column = higher_range
    pass_id = row * 8 + column
    seen_ids.append(pass_id)
    if pass_id > highest_id:
        highest_id = pass_id

print(highest_id)

seen_ids.sort()
for i in range(1, len(seen_ids) - 1):
    if seen_ids[i] + 2 == seen_ids[i + 1]:
        print(seen_ids[i] + 1)