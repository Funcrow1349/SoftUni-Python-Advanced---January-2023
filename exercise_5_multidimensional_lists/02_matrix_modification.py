#   Write a program that reads a matrix from the console and changes its values. On the first line, you will get the
#   matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space.
#   You will be receiving commands in the following format:
#   •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
#   •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
#   If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given
#   indexes are in range [0; len() – 1].
#   When you receive "END", you should print the matrix and stop the program.


def add_func(some_matrix, x, y, z):
    some_matrix[x][y] += z


def subtract_func(some_matrix, x, y, z):
    some_matrix[x][y] -= z


def coordinate_validator(some_matrix, x, y):
    if 0 <= x < len(some_matrix) and 0 <= y < len(some_matrix[x]):
        return True
    return False


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    current_command = input().split()
    if current_command[0] == "END":
        break
    command = current_command[0]
    coord1, coord2, value = int(current_command[1]), int(current_command[2]), int(current_command[3])
    if coordinate_validator(matrix, coord1, coord2):
        if command == "Add":
            add_func(matrix, coord1, coord2, value)
        elif command == "Subtract":
            subtract_func(matrix, coord1, coord2, value)
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)

