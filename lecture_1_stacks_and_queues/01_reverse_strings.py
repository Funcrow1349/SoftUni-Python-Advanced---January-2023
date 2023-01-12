# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console

some_string = list(input())
for char in range(len(some_string)):
    print(some_string.pop(), end="")


