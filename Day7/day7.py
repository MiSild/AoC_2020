from file_helper import *
import copy

rows = [row.strip() for row in read_text_into_list()]
"""rows = ["shiny gold bags contain 2 dark red bags.",
"dark red bags contain 2 dark orange bags.",
"dark orange bags contain 2 dark yellow bags.",
"dark yellow bags contain 2 dark green bags.",
"dark green bags contain 2 dark blue bags.",
"dark blue bags contain 2 dark violet bags.",
"dark violet bags contain no other bags."]"""
bags_list = []
bags_dict = {}

goal = "shiny gold"

for row in rows:
    line = row.split(" bags contain ")
    new_bag = line[0]
    contains = line[1].split(",")
    new_bag_list = []
    for contain_bag in contains:
        number = [int(s) for s in contain_bag.split() if s.isdigit()]
        if len(number) != 0:
            number = number[0]
            bag_type = contain_bag.split()[1:-1]
            bag_type = " ".join(bag_type)
            new_bag_list.append([bag_type, number])
    bags_list.append(new_bag)
    bags_dict[new_bag] = new_bag_list

bags_count = {}

def can_contain(bag):
    for child in bags_dict[bag]:
        if child[0] == goal:
            return True
        elif can_contain(child[0]):
            bags_count[child[0]] = 1
            return True
        else:
            bags_count[child[0]] = 0
    return False

for bag in bags_list:
    if bag in bags_count:
        continue
    else:
        if can_contain(bag):
            bags_count[bag] = 1
        else:
            bags_count[bag] = 0

summa = 0
for value in bags_count.values():
    summa += value

print(summa)
bags_hold = {}
summa = 0


def number_of_child_bags(bag):
    child_sum = 0
    for child in bags_dict[bag]:
        if child[0] in bags_hold:
            child_sum += child[1] * bags_hold[child[0]] + child[1]
        elif len(bags_dict[child[0]]) == 0: # No other children
            child_sum += child[1]
            bags_hold[child[0]] = 0
        else:
            child_sum += child[1] * number_of_child_bags(child[0]) + child[1]
    bags_hold[bag] = child_sum
    return child_sum

for bag_list in bags_dict[goal]:
    summa += bag_list[1] * number_of_child_bags(bag_list[0]) + bag_list[1]

print(summa)