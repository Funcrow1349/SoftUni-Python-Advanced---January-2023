#   Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one
#   in the examples below.
#   •	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
#   •	Columns + rows define the middle letter:
#       o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
#       o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
#   Input
#   •	The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
#   •	r and c are integers in the range [1, 26]

rows, columns = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    sub_matrix = []
    for j in range(columns):
        sub_matrix.append(chr(97 + i) + chr(97 + i + j) + chr(97 + i))
    matrix.append(sub_matrix)

for row in range(rows):
    print(*matrix[row])

