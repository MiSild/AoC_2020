from file_helper import *
import copy

rows = [row.strip() for row in read_text_into_list()]

letters = [chr(i) for i in range(97, 123)]
# rows = ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b",""]

sum_of_yes = 0
group_yes = 0
unanswered = copy.deepcopy(letters)
for row in rows:
    if row =="":
        sum_of_yes += group_yes
        group_yes = 0
        unanswered = copy.deepcopy(letters)
    else:
        for letter in row:
            if letter in unanswered:
                group_yes += 1
                unanswered.remove(letter)

print(sum_of_yes)

sum_of_yes = 0
unanswered = copy.deepcopy(letters)
for row in rows:
    if row =="":
        sum_of_yes += len(unanswered)
        unanswered = copy.deepcopy(letters)
    else:
        seen_letters = []
        for letter in unanswered:
            if letter in row:
                seen_letters.append(letter)
        unanswered = seen_letters

print(sum_of_yes)