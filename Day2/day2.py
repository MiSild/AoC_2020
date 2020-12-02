from file_helper import *

passwords = [i.split(" ") for i in read_text_into_list()]
valid_passwords = 0
first_task = False

if first_task:
    for password in passwords:
        password[0] = [int(i) for i in password[0].split("-")]
        lower_bound = password[0][0]
        upper_bound = password[0][1]
        password[1] = password[1].split(":")[0]
        password[2] = password[2].strip()
        if not (password[2].count(password[1]) > upper_bound or password[2].count(password[1]) < lower_bound):
            valid_passwords += 1
else:
    for password in passwords:
        password[0] = [int(i) for i in password[0].split("-")]
        first_occurence = password[0][0]
        second_occurence = password[0][1]
        password[1] = password[1].split(":")[0]
        password[2] = password[2].strip()
        if (password[2][first_occurence-1] == password[1]) ^ (password[2][second_occurence-1] == password[1]):
            valid_passwords += 1

print(valid_passwords)
