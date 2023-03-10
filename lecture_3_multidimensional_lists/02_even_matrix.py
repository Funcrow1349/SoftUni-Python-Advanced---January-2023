#   Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even.
#   Use nested comprehension for that problem.
#   On the first line, you will receive the rows of the matrix. On the next rows, you will get elements for each column
#   separated with a comma and a space ", ".


rows = int(input())
even_matrix = []

for row in range(rows):
    even_matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])

print(even_matrix)