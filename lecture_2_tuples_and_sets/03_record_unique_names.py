# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

number_of_names = int(input())
list_of_names = {input() for name in range(number_of_names)}

for name in list_of_names:
    print(name)