#   Write function called best_list_pureness which will receive a list of numbers and a number K. You have to rotate the
#   list K times (last becomes first) to find the variation of the list with the best pureness (pureness is calculated
#   by summing all the elements in the list multiplied by their indices). For example, in the list [4, 3, 2, 6] with
#   the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. At the end the function should return a string
#   containing the highest pureness and the amount of rotations that were made to find this pureness in the following
#   format: "Best pureness {pureness_value} after {count_rotations} rotations". If there is more than one highest
#   pureness, take the first one.
#
#   Input
#   •	There will be no input, just parameters passed to your function
#   Output
#   •	There is no expected output
#   •	The function should return a string in the following format:
#       "Best pureness {pureness_value} after {count_rotations} rotations"

from collections import deque


def best_list_pureness(some_list, number):
    max_pureness = 0
    rotations = 0
    some_list = deque(some_list)
    for k in range(number + 1):
        pureness = 0

        for i in range(len(some_list)):
            pureness += some_list[i] * i

        if pureness > max_pureness:
            max_pureness = pureness
            rotations = k

        some_list.appendleft(some_list.pop())

    return f"Best pureness {max_pureness} after {rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
