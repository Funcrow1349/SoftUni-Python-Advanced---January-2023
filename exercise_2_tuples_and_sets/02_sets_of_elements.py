# Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, separated by
# a single space - representing the lengths of two separate sets. On the next n + m lines, you will receive n numbers,
# which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that
# appear in both and print them on separate lines (the order does not matter).
# For example:
#   Set with length n = 4: {1, 3, 5, 7}
#   Set with length m = 3: {3, 4, 5}
#   Set that contains all the elements that repeat in both sets -> {3, 5}

def lengths_func():
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    return num1, num2


def fill_sets(length_one, length_two):
    set_one = set()
    set_two = set()
    for num in range(length_one):
        current_number = int(input())
        set_one.add(current_number)
    for num in range(length_two):
        current_number = int(input())
        set_two.add(current_number)
    return set_one, set_two


first_set_length, second_set_length = lengths_func()
first_set, second_set = fill_sets(first_set_length, second_set_length)
result = first_set & second_set
for element in result:
    print(element)


