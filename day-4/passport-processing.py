# import input data
passport_structure = {
        'ecl': None, 'pid': None, 'eyr': None, 'hcl': None,
        'byr': None, 'iyr': None, 'cid': None, 'hgt': None
}
passports = []
with open('input.txt', 'r') as f:
    passport = passport_structure.copy()  # create a copy of the passport structure
    for line in f:
        if line == '\n':  # if blank line, store the passport and pull in an empty one
            passports.append(passport)
            passport = passport_structure.copy()
        else:  # if not a blank line, fill details into the current passport
            for item in line.split():
                passport[item[0:3]] = item[4:]
f.close()


# Part 1
p1_valid_passports = []
# if any of the fields are empty, return passport as invalid
for passport in passports:
    valid = True
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if passport[field] is None:
            valid = False

    if valid:
        p1_valid_passports.append(passport)

print("There are {} valid passports for part 1.".format(len(p1_valid_passports)))


# Part 2
def check_passport(passport):
    """ checks a passport's fields for validity

    :param passport: (dict) the passport to check
    :return: (bool) whether or not the passport is valid
    """
    # check that birth year is between 1920 and 2002
    if int(passport['byr']) not in range(1920, 2003):
        return False

    # check that issue year is between 2020 and 2020
    if int(passport['iyr']) not in range(2010, 2021):
        return False

    # check that expiration year is between 2020 and 2030
    if int(passport['eyr']) not in range(2020, 2031):
        return False

    # check that height ends in either 'cm' or 'in'
    if passport['hgt'][-2:] == 'cm':
        # check that height is between 150 and 193
        if int(passport['hgt'][:-2]) not in range(150, 194):
            return False
    elif passport['hgt'][-2:] == 'in':
        # check that height is between 59 and 76
        if int(passport['hgt'][:-2]) not in range(59, 77):
            return False
    else:
        return False

    # check that hair colour begins with '#' and has a length of 7
    if (passport['hcl'][0] != '#') or (len(passport['hcl']) != 7):
        return False

    # check that the last 6 digits of hair colour are either 0-9 or a-f
    for char in passport['hcl'][1:]:
        if not char.isnumeric():  # if char is not numeric
            if char not in ['a', 'b', 'c', 'd', 'e', 'f']:
                return False

    # check that eye colour is valid
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    # check that passport id is a nine-digit integer
    if (len(passport['pid']) != 9) or not passport['pid'].isnumeric():
        return False

    return True


p2_valid_passports = []
for passport in p1_valid_passports:
    if check_passport(passport):
        p2_valid_passports.append(passport)

print("There are {} valid passports for part 2.".format(len(p2_valid_passports)))
