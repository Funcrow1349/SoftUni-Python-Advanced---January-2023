#   Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines,
#   you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol.
#   Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
#   You should start searching from the top left. If there is no such symbol, print the message "{symbol} does not occur
#   in the matrix".

rows = int(input())
matrix = [[x for x in list(input())] for row in range(rows)]
special_symbol = input()
special_symbol_location = ()

for row in range(len(matrix)):
    if special_symbol_location:
        break
    for column in range(len(matrix[row])):
        current_element = matrix[row][column]
        if current_element == special_symbol:
            special_symbol_location = (row, column)
            break


if special_symbol_location:
    print(special_symbol_location)
else:
    print(f"{special_symbol} does not occur in the matrix")