from collections import deque

initial_string = deque(input().split())
colors = []

while len(initial_string) >= 2:
    first_segment = initial_string.popleft()
    second_segment = initial_string.pop()
    full_segment = first_segment + second_segment
    full_segment_two = second_segment + first_segment
    if full_segment in ["red", "yellow", "blue", "orange", "purple", "green"]:
        colors.append(full_segment)
    elif full_segment_two in ["red", "yellow", "blue", "orange", "purple", "green"]:
        colors.append(full_segment_two)
    else:
        first_segment = first_segment[:-1]
        second_segment = second_segment[:-1]
        middle_of_the_string = len(initial_string) // 2
        if first_segment:
            initial_string.insert(middle_of_the_string - 1, first_segment)
        if second_segment:
            initial_string.insert(middle_of_the_string, second_segment)

if initial_string:
    while initial_string[0] != "":
        if initial_string[0] in ["red", "yellow", "blue", "orange", "purple", "green"]:
            colors.append(initial_string[0])
            initial_string.pop()
            break
        else:
            initial_string[0] = initial_string[0][:-1]

for color in colors:
    if color == "orange":
        if "yellow" not in colors or "red" not in colors:
            colors.remove(color)
    elif color == "purple":
        if "blue" not in colors or "red" not in colors:
            colors.remove(color)
    elif color == "green":
        if "yellow" not in colors or "blue" not in colors:
            colors.remove(color)

print(colors)
