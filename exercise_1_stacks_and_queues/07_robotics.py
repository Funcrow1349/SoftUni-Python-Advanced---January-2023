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

    if int(robot_factory[0][2]) == 0:
        robot_factory[0][2] = robot_factory[0][1]
        print(f"{robot_factory[0][0]} - {product} [{factory_time}]")
        robot_factory.rotate(-1)
    else:
        robot_factory[0][2] -= 1
        robot_factory.rotate(-1)
        products.append(product)