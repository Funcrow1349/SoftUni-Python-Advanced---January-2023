#   Write a program that reads a matrix from the console and performs certain operations with its elements. User input
#   is provided similarly to the problems above - first, you read the dimensions and then the data.
#   Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and
#   ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword
#   along with four valid coordinates (no more, no less), separated by a single space.
#   •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step
#       (thus, you will be able to check if the operation was performed correctly).
#   •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the
#       given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value
#       makes the coordinates not valid.
#   Your program should finish when the command "END" is entered.

rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for row in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    for i in range(1, 5):
        if command[i].isdigit():
            command[i] = int(command[i])
        else:
            print("Invalid input!")
            continue

    if command[1] < rows and command[2] < columns and command[3] < rows and command[4] < columns:
        matrix[command[1]][command[2]], matrix[command[3]][command[4]] = \
            matrix[command[3]][command[4]], matrix[command[1]][command[2]]
        for row in range(rows):
            print(*matrix[row])

    else:
        print("Invalid input!")
