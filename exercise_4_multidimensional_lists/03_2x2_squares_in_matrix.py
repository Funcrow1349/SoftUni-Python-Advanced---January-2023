#   Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the
#   matrix's dimensions in the format "{rows} {columns}". On the following rows, you will receive characters separated
#   by a single space. Print the number of all square matrices you have found.

rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]
perfect_squares = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        upper_left = matrix[i][j]
        upper_right = matrix[i][j + 1]
        lower_left = matrix[i + 1][j]
        lower_right = matrix[i + 1][j + 1]
        if upper_left == upper_right == lower_left == lower_right:
            perfect_squares += 1

print(perfect_squares)