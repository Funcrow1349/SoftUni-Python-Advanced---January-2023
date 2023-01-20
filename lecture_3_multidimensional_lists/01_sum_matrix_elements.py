#   Write a program that reads a matrix from the console and prints:
#   •	The sum of all numbers in the matrix
#   •	The matrix itself
#   On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows, you will
#   get elements for each column separated by a comma and a space ", ".

rows, columns = [int(x) for x in input().split(", ")]

matrix = []
total_sum = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
    total_sum += sum(matrix[row])

print(total_sum)
print(matrix)