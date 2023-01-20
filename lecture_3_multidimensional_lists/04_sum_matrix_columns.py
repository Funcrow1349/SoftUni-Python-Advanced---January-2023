#   Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
#   On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements
#   for each column separated with a single space.

rows, columns = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(" ")] for row in range(rows)]

for column in range(columns):
    current_column_sum = 0
    for row in range(rows):
        current_column_sum += matrix[row][column]
    print(current_column_sum)