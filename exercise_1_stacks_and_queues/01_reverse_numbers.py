# Write a program that reads a string with N integers from the console, separated by a single space, and reverses them
# using a stack. Print the reversed integers on one line, separated by a single space.

stack_of_integers = input().split(" ")
for i in range(len(stack_of_integers)):
    print(stack_of_integers.pop(), end=" ")