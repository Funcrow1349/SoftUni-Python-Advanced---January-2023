# First, you will be given two sequences of integers values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
#   •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
#   •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
#   •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
#   •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
#   •	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True".
#       Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ".
# The values in each sequence should be sorted in ascending order.

first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
number_of_commands = int(input())

for _ in range(number_of_commands):
    current_command = input().split(" ")
    numbers = set([int(x) for x in current_command if x.isdigit()])
    if current_command[0] == "Add" and current_command[1] == "First":
        for x in numbers:
            first_sequence.add(x)
    elif current_command[0] == "Add" and current_command[1] == "Second":
        for x in numbers:
            second_sequence.add(x)
    elif current_command[0] == "Remove" and current_command[1] == "First":
        for x in numbers:
            first_sequence.discard(x)
    elif current_command[0] == "Remove" and current_command[1] == "Second":
        for x in numbers:
            second_sequence.discard(x)
    else:
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
