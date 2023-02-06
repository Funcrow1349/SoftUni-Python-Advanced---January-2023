#   You are visiting Santa Claus' workshop, and it is complete chaos. You will need to help Santa find all items
#   scattered around the workshop.
#   You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented
#   as some symbols separated by a single space:
#   •	Your position is marked with the symbol "Y"
#   •	Christmas decorations are marked with the symbol "D"
#   •	Gifts are marked with the symbol "G"
#   •	Cookies are marked with the symbol "C"
#   •	All of the empty positions will be marked with "."
#   After the field state, you will be given commands until you receive the command "End". The commands will be in the
#   format "right/left/up/down-{steps}". You should move in the given direction with the given steps and collect all
#   the items that come across. If you go out of the field, you should continue to traverse the field from the opposite
#   side in the same direction. You should mark your path with "x". Your current position should always be marked
#   with "Y".
#   Keep track of all collected items. If you've collected all items at any point, end the program and print:
#   "Merry Christmas!".
#   Input
#   •	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
#   •	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
#   •	On the following lines, you will receive commands in the format described above until you receive the command
#       "End" or until you collect all items.
#   Output
#   •	On the first line, if you have collected all items, print:
#       o	"Merry Christmas!"
#       o	Otherwise, skip the line
#   •	Next, print the number of collected items in the format:
#       o	"You've collected:
#       o	- {number_of_decoration} Christmas decorations
#       o	- {number_of_gifts} Gifts
#       o	- {number_of_cookies} Cookies"
#   •	Finally, print the field, as shown in the examples.
#   Constrains
#   •	All the commands will be valid
#   •	There will always be at least one item
#   •	The dimensions of the matrix will be integers in the range [1, 20]
#   •	The field will always have only one "Y"
#   •	On the field, there will always be only the symbols shown above.

rows, columns = [int(x) for x in input().split(", ")]
workshop = []
my_pos = []
all_items = 0

for i in range(rows):
    row = input().split()
    workshop.append(row)

    if "Y" in row:
        my_pos = [i, row.index("Y")]
        workshop[my_pos[0]][my_pos[1]] = "x"
    all_items += row.count("D")
    all_items += row.count("G")
    all_items += row.count("C")

decorations = 0
gifts = 0
cookies = 0

directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

while all_items:
    command = input().split("-")
    if command[0] == "End":
        workshop[my_pos[0]][my_pos[1]] = "Y"
        break

    direction = command[0]
    steps = int(command[1])

    for step in range(steps):
        row, col = my_pos[0] + directions[direction][0], my_pos[1] + directions[direction][1]
        if row < 0:
            row = rows - 1
        elif row == rows:
            row = 0
        if col < 0:
            col = columns - 1
        elif col == columns:
            col = 0

        if workshop[row][col] == "D":
            decorations += 1
            all_items -= 1
        elif workshop[row][col] == "G":
            gifts += 1
            all_items -= 1
        elif workshop[row][col] == "C":
            cookies += 1
            all_items -= 1

        workshop[row][col] = "x"
        my_pos = [row, col]

        if not all_items:
            workshop[row][col] = "Y"
            print("Merry Christmas!")
            break

print(f"You've collected:\n- {decorations} Christmas decorations\n- {gifts} Gifts\n- {cookies} Cookies")
for row in workshop:
    print(*row, sep=" ")


