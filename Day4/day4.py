from file_helper import *
import copy, re
rows = read_text_into_list()
rows = [row.strip() for row in rows]

def split_on_letter(s):
    match = re.compile("[^\W\d]").search(s)
    if match is None:
        return [0,0]
    return [s[:match.start()], s[match.start():]]

def valid_hair(s):
    if s[0] == "#":
        for i in range(1, len(s)):
            if s[i] not in ["0", "1","2","3","4","5","6","7","8","9", "a","b","c","d","e","f"]:
                return False
        return True
    return False

fields = ["byr",
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid"]
optional_field = "cid"
unch_fields = copy.deepcopy(fields)
found_fields = 0
wanted_fields = 7
found_cid = False
valid_passports = 0
for row in rows:
    if row == "":
        unch_fields = copy.deepcopy(fields)
        if found_fields < wanted_fields:
            found_fields = 0
            continue
        else:
            found_fields = 0
            valid_passports += 1
            continue
    else:
        new_fields = row.split(" ")
        for field in new_fields:
            if field.split(":")[0] in unch_fields:
                found_fields += 1

                unch_fields.remove(field.split(":")[0])
if found_fields < wanted_fields:
    found_fields = 0
else:
    found_fields = 0
    valid_passports += 1
print(valid_passports)

unch_fields = copy.deepcopy(fields)
found_fields = 0
wanted_fields = 7
valid_passports = 0

for row in rows:
    if row == "":
        unch_fields = copy.deepcopy(fields)
        if found_fields < wanted_fields:
            found_fields = 0
            continue
        else:
            found_fields = 0
            valid_passports += 1
            continue
    else:
        new_fields = row.split(" ")
        for field in new_fields:
            check_field = field.split(":")[0]
            if check_field in unch_fields:
                if check_field == "byr" and (int(field.split(":")[1]) >= 1920 and int(field.split(":")[1]) <= 2002):
                    found_fields += 1
                elif check_field == "iyr" and (int(field.split(":")[1]) >= 2010 and int(field.split(":")[1]) <= 2020):
                    found_fields += 1
                elif check_field == "eyr" and (int(field.split(":")[1]) >= 2020 and int(field.split(":")[1]) <= 2030):
                    found_fields += 1
                elif check_field == "hgt":
                    height_type = split_on_letter(field.split(":")[1])
                    if (height_type[1] == "in" and int(height_type[0]) >= 59 and int(height_type[0]) <= 76) or (height_type[1] == "cm" and int(height_type[0]) >= 150 and int(height_type[0]) <= 193):
                        found_fields += 1
                elif check_field == "hcl" and valid_hair(field.split(":")[1]):
                    found_fields += 1
                elif check_field == "ecl" and field.split(":")[1] in ["amb", "blu", "brn", "gry","grn", "hzl", "oth"]:
                    found_fields += 1
                elif check_field == "pid" and len(field.split(":")[1]) == 9 and field.split(":")[1].isdecimal():
                    found_fields += 1
                unch_fields.remove(field.split(":")[0])


print(valid_passports)