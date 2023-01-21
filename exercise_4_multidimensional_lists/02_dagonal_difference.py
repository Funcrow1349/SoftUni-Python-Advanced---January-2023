#   Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
#   On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the
#   values for each column - N numbers separated by a single space. Print the absolute difference between the primary
#   and the secondary diagonal sums.

rows = int(input())
matrix = [[int(x) for x in input().split(" ")]for row in range(rows)]
primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[(rows - 1) - i][i] for i in range(rows - 1, -1, -1)]

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)