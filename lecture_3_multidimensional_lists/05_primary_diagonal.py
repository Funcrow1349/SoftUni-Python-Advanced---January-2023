#   Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom
#   right).
#   On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the values
#   for each column - N numbers, separated by a single space.

rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]
primary_sum = 0

for row in range(rows):
    primary_sum += matrix[row][row]

print(primary_sum)