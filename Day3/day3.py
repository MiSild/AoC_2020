from file_helper import *


def is_tree(character):
    return character == "#"


tree_map = read_text_into_list()
tree_map = [[is_tree(x) for x in i.strip()] for i in tree_map]
rows = len(tree_map)
columns = len(tree_map[0])
tree_count = 0
tree_mult = 1
right_step = 3
down_step = 1
column = -3
rights = [1,3,5,7,1]
downs = [1,1,1,1,2]
for k in range(5):
    right_step = rights[k]
    down_step = downs[k]
    column = -right_step
    tree_count = 0
    for i in range(0, rows, down_step):
        column = (column + right_step) % columns
        if tree_map[i][column]:
            tree_count += 1
    tree_mult = tree_mult * tree_count

print(tree_mult)