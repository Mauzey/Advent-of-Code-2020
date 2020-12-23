from functools import reduce

# import input data
slope = []
with open('input.txt', 'r') as f:
    # create a matrix of 1s and 0s where 1=tree and 0=empty space
    for line in f:
        line_mtx = []
        for char in line:
            if char == '.':
                line_mtx.append(0)
            elif char == '#':
                line_mtx.append(1)

        slope.append(line_mtx)
f.close()


def get_tree_count(right_n, down_n, slope=slope):
    current_row = 0
    current_col = 0
    n_trees = 0

    while current_row <= (len(slope) - 1):
        # check if the current position is a tree
        if slope[current_row][current_col] == 1:
            n_trees += 1

        # get the distance between the current column and the end of the row
        col_diff = (len(slope[current_row])) - current_col

        # if moving right by 'right_n' leaves us out of bounds, loop the slope
        if (current_col + right_n) > (len(slope[current_row]) - 1):
            current_col = 0 + (right_n - col_diff)
        else:
            current_col += right_n

        current_row += down_n

    return n_trees


# Part 1
print("The number of trees encountered for part one:", get_tree_count(3, 1))


# Part 2
part_2 = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

part_2_results = []
for x in part_2:
    part_2_results.append(get_tree_count(x[0], x[1]))

part_2_ans = reduce((lambda x, y: x * y), part_2_results)
print("The answer for part two: ", part_2_ans)
