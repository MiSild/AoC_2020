from file_helper import *
import re

commands = [row.strip() for row in read_text_into_list()]

x_cord = 0
y_cord = 0
direction = 0  # 0 east, 90 S, 180 W, 270 N, 360 E again and so on
direction_to_l = {0: "E", 90: "S", 180: "W", 270: "N"}


def execute_command(command, value):
    global y_cord, x_cord, direction
    if command == "N":
        y_cord += value
    elif command == "S":
        y_cord -= value
    elif command == "E":
        x_cord += value
    elif command == "W":
        x_cord -= value
    elif command == "R":
        direction = (direction + value) % 360
    elif command == "L":
        direction = (direction - value) % 360
    elif command == "F":
        execute_command(direction_to_l[direction], value)


for line in commands:
    execute_command(re.split(r'(^[^\d]+)', line)[1:][0], int(re.split(r'(^[^\d]+)', line)[1:][1]))

print(abs(x_cord) + abs(y_cord))

x_cord = 0
y_cord = 0
w_y = 1
w_x = 10


def rotate(value):
    global w_y, w_x
    if value == 180:
        w_y = -w_y
        w_x = -w_x
    elif value == 90:
        w_x_c = w_x
        w_x = w_y
        w_y = -w_x_c
    elif value == 270:
        w_x_c = w_x
        w_x = -w_y
        w_y = w_x_c


def execute_command(command, value):
    global y_cord, x_cord, w_x, w_y
    if command == "N":
        w_y += value
    elif command == "S":
        w_y -= value
    elif command == "E":
        w_x += value
    elif command == "W":
        w_x -= value
    elif command == "R":
        rotate(value)
    elif command == "L":
        if value == 180:
            rotate(180)
        else:
            rotate((value + 180) % 360)
    elif command == "F":
        y_cord += w_y * value
        x_cord += w_x * value


for line in commands:
    execute_command(re.split(r'(^[^\d]+)', line)[1:][0], int(re.split(r'(^[^\d]+)', line)[1:][1]))

print(abs(x_cord) + abs(y_cord))
