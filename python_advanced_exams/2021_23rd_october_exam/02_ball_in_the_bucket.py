def check_prize(points):
    message = ""
    if points >= 100:
        message += f"Good job! You scored {points} points, and you've won "
        if 100 <= points <= 199:
            message += "Football."
        elif 200 <= points <= 299:
            message += "Teddy Bear."
        elif points >= 300:
            message += "Lego Construction Set."
    else:
        message = f"Sorry! You need {100 - points} points more to win a prize."

    return message


playground_size = 6
nr_of_throws = 3
total_points = 0

playground = [[int(x) if x.isdigit() else str(x) for x in input().split()] for row in range(playground_size)]

for throw in range(nr_of_throws):
    coordinates = input()
    coordinates = coordinates.replace("(", "")
    coordinates = coordinates.replace(")", "")
    row, col = [int(x) for x in coordinates.split(", ")]

    if 0 <= row < len(playground) and 0 <= col < len(playground):
        if playground[row][col] == "B":
            playground[row][col] = 0
            total_points += sum(playground[row][col] for row in range(0, playground_size))

print(check_prize(total_points))



