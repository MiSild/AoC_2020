from file_helper import *
from math import lcm

rows = [row.strip() for row in read_text_into_list()]
start_timestamp = int(rows[0])

buses_freq = [int(x) for x in rows[1].split(",") if x != "x"]
buses_first = {}

for freq in buses_freq:
    time = 0
    while time < start_timestamp:
        time += freq
    buses_first[freq] = time

diff = float("inf")
best_bus = 0

for bus in buses_first.keys():
    if buses_first[bus] - start_timestamp < diff:
        diff = buses_first[bus] - start_timestamp
        best_bus = bus

print(diff * best_bus)


def find_smallest_time(start_time, b_list, step):
    step = max(step, lcm(*b_list[:-1]))  # The minimum step is the lcm of the last subgroups buses, for one bus it is 1
    while True:
        curr_time = start_time
        found = True
        for bus in bus_freq[:bus_freq.index(str(b_list[-1])) + 1]:  # We only check up to the last bus in our list
            if bus == "x":
                curr_time += 1
            elif curr_time % int(bus) == 0:
                curr_time += 1
            else:
                found = False
                break
        if found:
            return start_time
        else:
            start_time += step
            continue


smallest_time = 100000000000000

bus_freq = [x for x in rows[1].split(",")]
bus_list = []

for bus in buses_freq:
    bus_list.append(bus)
    smallest_time = find_smallest_time(smallest_time, bus_list, 1)

print(smallest_time)