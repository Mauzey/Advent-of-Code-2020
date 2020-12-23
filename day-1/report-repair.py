# import input values
with open('input.txt', 'r') as f:
    values = [int(val) for val in f]
f.close()


# Part 1:
x, y = 0, 0
for val in values:
    if (2020 - val) in values:
        x = val
        y = 2020 - val

print("x = {}, y = {}".format(x, y))
print("Answer = ", x * y)


# Part 2:
x, y, z = 0, 0, 0
for val in values:
    for val2 in values:
        if 2020 - (val+val2) in values:
            x = val
            y = val2
            z = 2020 - (val+val2)

print("x = {}, y = {}, z = {}".format(x, y, z))
print("Answer = ", x * y * z)
