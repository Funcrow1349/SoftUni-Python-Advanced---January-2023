# The super-spy action hero Sam has finally found some time to go on a holiday. He is taking his wife somewhere nice,
# and they're going to have a really good time, but first, they have to get there. Even on his holiday trip, Sam is
# still going to run into some problems, and the first one is getting to the airport. Right now, he is stuck in a
# traffic jam at a crossroads where a lot of accidents happen.
# Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed the
# crossroads safely. Sam is on a single lane of cars that queue until the light goes green. When it does, they start
# passing one by one on a flashing green light and during the free window before the intersecting road's light goes
# green. For each second, only one part of a car (a single character) passes the crossroad. If a car is still in the
# middle of the crossroads when the free window ends, it will get hit at the first character that is still in the
# crossroads.
# Input
#   •	On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
#   •	On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
#   •	On the following lines, until you receive the "END" command, you will receive one of two things:
#   	A car - a string containing the model of the car, or
#   	The command "green" that indicates the start of a green light cycle
#       A green light cycle goes as follows:
#           •  	During the green light, cars will enter and exit the crossroads one by one
#           •	During the free window, cars will only exit the crossroads
# Output
#   •	If a crash happens, end the program and print:
#       "A crash happened!"
#       "{car} was hit at {character_hit}."
#   •	If everything goes smoothly and you receive an "END" command, print:
#       "Everyone is safe."
#       "{total_cars_passed} total cars passed the crossroads."
# Constraints
#   •	The input will be within the constraints specified above and will always be valid.
#       There is no need to check it explicitly.

from collections import deque

duration_of_green_light = int(input())
free_window = int(input())
cars = deque()

COMMAND_END = "END"
COMMAND_GREEN = "green"
crashes = False
total_cars_passed = 0

while True:
    current_command = input()
    if current_command == COMMAND_END:
        if not crashes:
            print("Everyone is safe.")
            print(f"{total_cars_passed} total cars passed the crossroads.")
        break
    elif current_command == COMMAND_GREEN:
        green_window = duration_of_green_light
        while green_window and cars:
            current_car = cars.popleft()
            if green_window >= len(current_car):
                green_window -= len(current_car)
                total_cars_passed += 1
            else:
                if green_window + free_window >= len(current_car):
                    green_window = 0
                    total_cars_passed += 1
                else:
                    crashed_index = green_window + free_window
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[crashed_index]}.")
                    crashes = True
                    break
        if crashes:
            break
    else:
        cars.append(current_command)