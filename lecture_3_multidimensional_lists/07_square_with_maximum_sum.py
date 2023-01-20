#   Write a program that reads a matrix from the console and finds the 2x2 top-left sub-matrix with biggest sum of its
#   values.
#   On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows, you will get elements for
#   each column, separated with a comma and a space ", ".
#   You should print the found sub-matrix and the sum of its elements, as shown in the examples.

rows, columns = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]
squares = {}

for row in range(rows - 1):
    for column in range(columns - 1):
        upper_left = matrix[row][column]
        upper_right = matrix[row][column + 1]
        lower_left = matrix[row + 1][column]
        lower_right = matrix[row + 1][column + 1]
        result = upper_left + upper_right + lower_left + lower_right
        if result not in squares.keys():
            squares[result] = [[upper_left, upper_right], [lower_left, lower_right]]

max_result = max(squares.keys())

upper, lower = squares[max_result]
print(*upper)
print(*lower)
print(max_result)
