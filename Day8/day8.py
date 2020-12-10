from file_helper import *
import copy

rows = [row.strip() for row in read_text_into_list()]

accumulator = 0
index = 0
seen_lines = []
no_twice = True
while no_twice:
    if index in seen_lines:
        no_twice = False
        print(accumulator)
        break

    seen_lines.append(index)
    instruction = rows[index].split()
    operation = instruction[0]
    argument = int(instruction[1])
    if operation == "nop":
        index += 1
    elif operation == "acc":
        index += 1
        accumulator += argument
    elif operation == "jmp":
        index += argument


def run_changed_rows(swap_index):
    lines = copy.deepcopy(rows)
    if lines[swap_index].split()[0] == "jmp":
        lines[swap_index] = "nop " + lines[swap_index].split()[1]
    else:
        lines[swap_index] = "jmp " + lines[swap_index].split()[1]

    accumulator = 0
    index = 0
    seen_lines = []

    while index != len(rows):
        if index in seen_lines or index > len(rows):
            return

        seen_lines.append(index)
        instruction = lines[index].split()
        operation = instruction[0]
        argument = int(instruction[1])
        if operation == "nop":
            index += 1
        elif operation == "acc":
            index += 1
            accumulator += argument
        elif operation == "jmp":
            index += argument
    print(accumulator)


for row in range(len(rows)):
    if rows[row].split()[0] == "jmp" or rows[row].split()[0] == "nop":
        run_changed_rows(row)