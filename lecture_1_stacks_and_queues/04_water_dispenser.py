# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following
# lines, you will be given the names of some people who want to get water (each on a separate line) until you receive
# the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
#   -	"{liters}" - litters (integer) that the current person in the queue wants to get.
#       Check if there is enough water in the dispenser for that person.
#       o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
#       o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water
#           in the dispenser.
#   -	"refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".

from collections import deque
litres_of_water = int(input())
people_queue = deque()
while True:
    current_command = input()
    if current_command == "Start":
        break
    else:
        people_queue.append(current_command)

while True:
    command = input()
    if command == "End":
        print(f"{litres_of_water} liters left")
        break
    elif "refill" in command:
        command = command.split(" ")
        litres = int(command[1])
        litres_of_water += litres
    else:
        command = int(command)
        if litres_of_water >= command:
            print(f"{people_queue.popleft()} got water")
            litres_of_water -= command
        else:
            print(f"{people_queue.popleft()} must wait")