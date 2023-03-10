#   The presents are ready, and Santa has to deliver them to the kids.
#   You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood
#   with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
#   Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live.
#   If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is
#   marked by "V". There can also be cells marked with "C" for cookies. All of the empty positions will be marked with
#   "-".
#   Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you
#   receive. If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a
#   naughty kid, he doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies
#   and becomes happy and extra generous to all the kids around him* (meaning all of them will receive presents - it
#   doesn't matter if naughty or nice). If Santa has been to a house, the cell becomes "-".
#   Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to
#   these cells, or if he does, he returns to the cell where the cookie was.
#   If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
#   Keep in mind that you should check whether all the nice kids received presents.
#   Input
#   •	On the first line, you are given the integer m - the count of presents
#   •	On the second - integer n - the size of the neighborhood
#   •	The following n lines hold the values for every row
#   •	On each of the following lines you will get a command
#   Output
#   •	On the first line:
#       o	If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
#   •	Next, print the matrix.
#   •	In the end, print one of these messages:
#       o	If he manages to give all the nice kids presents, print:
#           "Good job, Santa! {count_nice_kids} happy nice kid/s."
#       o	Otherwise, print:
#           "No presents for {count nice kids} nice kid/s."
#   Constraints
#   •	The size of the square matrix will be between [2…10].
#   •	Santa's position will be marked with 'S'.
#   •	There will always be at least 1 nice kid.
#   •	There won't be a case where the cookie is on the border of the matrix.

presents = int(input())
size = int(input())
neighbourhood = []
nice_kids = 0
kids_with_presents = 0
santa_pos = []

for row in range(size):
    neighbourhood.append(input().split())

    if "S" in neighbourhood[row]:
        santa_pos = [row, neighbourhood[row].index("S")]

    if "V" in neighbourhood[row]:
        nice_kids += neighbourhood[row].count("V")

directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

while presents:
    command = input()

    if command == "Christmas morning":
        break

    r = santa_pos[0] + directions[command][0]
    c = santa_pos[1] + directions[command][1]

    if 0 <= r < size and 0 <= c < size:
        neighbourhood[santa_pos[0]][santa_pos[1]] = "-"
        santa_pos = [r, c]
        position = neighbourhood[r][c]
        neighbourhood[r][c] = "S"

        if position == "V":
            kids_with_presents += 1
            presents -= 1

        elif position == "C":
            for direction in directions:
                row = r + directions[direction][0]
                col = c + directions[direction][1]
                if 0 <= row < size and 0 <= col < size:
                    if neighbourhood[row][col] == "V" or neighbourhood[row][col] == "X":
                        presents -= 1
                        if neighbourhood[row][col] == "V":
                            kids_with_presents += 1
                        neighbourhood[row][col] = "-"

if presents == 0 and kids_with_presents < nice_kids:
    print("Santa ran out of presents!")
for row in neighbourhood:
    print(*row, sep=" ")
if kids_with_presents < nice_kids:
    print(f"No presents for {nice_kids - kids_with_presents} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")




