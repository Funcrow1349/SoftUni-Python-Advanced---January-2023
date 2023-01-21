#   Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by
#   a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
#       "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
#       Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

rows = int(input())
matrix = [[int(x) for x in input().split(", ")]for row in range(rows)]
primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[(rows - 1) - i][i] for i in range(rows - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")


