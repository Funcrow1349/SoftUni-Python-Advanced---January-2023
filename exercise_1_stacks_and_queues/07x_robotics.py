# There is a robotics factory. The current project is assembly-line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product.
# When a robot is free, it should take a product for processing and log its name, product, and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second
# (so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free
# robot to take it, it should be queued at the end of the line again.
# The robots are standing in the line in the order of their appearance.
# Input
#   •	On the first line, you will receive the robots' names and their processing times in the format
#       "robotName-processTime;robotName-processTime;robotName-processTime..."
#   •	On the second line, you will get the starting time in the format "hh:mm:ss"
#   •	Next, until the "End" command, you will get a product on each line.
# Output
#   •	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

from collections import deque
from datetime import datetime, timedelta

robot_factory = deque()
robots = input().split(";")

for robot in robots:
    robot_name, time = robot.split("-")
    robot_factory.append([robot_name, int(time), 0])

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()
    for i in range(len(robot_factory)):
        if robot_factory[i][2] == 0:
            robot_factory[i][2] = robot_factory[i][1]
            print(f"{robot_factory[i][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")
            break
    else:
        products.append(product)

    for robot in robot_factory:
        robot[2] -= 1
        if robot[2] < 0:
            robot[2] = 0