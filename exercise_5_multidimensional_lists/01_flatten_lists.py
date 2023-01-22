#   Write a program to flatten several lists of numbers received in the following format:
#   	String with numbers or empty strings separated by "|"
#   	Values are separated by spaces (" ", one or several)
#   	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown
#       below

matrix = [row.split() for row in input().split("|")]
flattened_matrix = []
for row in range(len(matrix) - 1, - 1, - 1):
    flattened_matrix.extend(matrix[row])

print(*flattened_matrix)
