# import input data
passwords = []
with open('input.txt', 'r') as f:
    for line in f:
        split_line = line.split()

        passwords.append({
            'lower_thresh': int(split_line[0].split('-')[0]),
            'upper_thresh': int(split_line[0].split('-')[1]),
            'letter': split_line[1].replace(':', ''),
            'pwd_text': split_line[2]
        })
f.close()


# Part 1:
valid_passwords = 0
for password in passwords:
    # count letter occurrences
    letter_count = 0
    for char in password['pwd_text']:
        if char == password['letter']:
            letter_count += 1

    # check that the letter count is within bounds
    if letter_count >= password['lower_thresh']:
        if letter_count <= password['upper_thresh']:
            valid_passwords += 1

print("There are {} valid passwords for part 1.".format(valid_passwords))


# Part 2:
valid_passwords = 0
for password in passwords:
    first_letter = password['pwd_text'][password['lower_thresh'] - 1]
    second_letter = password['pwd_text'][password['upper_thresh'] - 1]

    if first_letter == second_letter:
        continue

    if (first_letter == password['letter']) or (second_letter == password['letter']):
        valid_passwords += 1

print("There are {} valid passwords for part 2.".format(valid_passwords))
