#   Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
#   You will receive a 6x6 field on separate lines with:
#   •	One rover - marked with the letter "E"
#   •	Water deposit (one or many) - marked with the letter "W"
#   •	Metal deposit (one or many) - marked with the letter "M"
#   •	Concrete deposit (one or many) - marked with the letter "C"
#   •	Rock (one or many) - marked with the letter "R"
#   •	Empty positions will be marked with "-"
#   After that, you will be given the commands for the rover's movement on one line separated by a comma and a space
#   (", "). Commands can be: "up", "down", "left", or "right".
#   For each command, the rover moves in the given directions with one step, and it can land on one of the given types
#   of deposit or a rock:
#   •	When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and
#       increase its value by 1.
#   •	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown
#       below, and the program ends.
#   •	If the rover goes out of the field, it should continue from the opposite side in the same direction. Example:
#       If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at
#       position (3, 5).
#   The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
#   Stop the program if you run out of commands or the rover gets broken.
#   Input
#   •	On the first 6 lines, you will receive the matrix.
#   •	On the following line, you will receive the commands for the rover separated by a comma and a space.
#   Output
#   •	For each deposit found while you go through the commands, print out on the console:
#       "{Water, Metal or Concrete} deposit found at ({row}, {col})"
#   •	If the rover hits a rock, print the coordinates where it got broken in the format:
#       "Rover got broken at ({row}, {col})"
#   After you go through all the commands or the rover gets broken, print out on the console:
#   •	If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
#   •	Otherwise, print on the console: "Area not suitable to start the colony."

mars_map = []
rover_position = []
water = 0
concrete = 0
metal = 0

for i in range(6):
    row = input().split()
    mars_map.append(row)
    if "E" in row:
        rover_position = [i, row.index("E")]

commands = input().split(", ")

directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

for command in commands:
    row, col = rover_position[0] + directions[command][0], rover_position[1] + directions[command][1]

    if row < 0:
        row = len(mars_map) - 1
    elif row == len(mars_map):
        row = 0
    elif col < 0:
        col = len(mars_map) - 1
    elif col == len(mars_map):
        col = 0

    rover_position = [row, col]
    if mars_map[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

    if mars_map[row][col] == "W":
        print(f"Water deposit found at ({row}, {col})")
        water += 1
    elif mars_map[row][col] == "C":
        print(f"Concrete deposit found at ({row}, {col})")
        concrete += 1
    elif mars_map[row][col] == "M":
        print(f"Metal deposit found at ({row}, {col})")
        metal += 1

if water and concrete and metal:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")









