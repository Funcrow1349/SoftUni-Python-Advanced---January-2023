first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])
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

print(*first_sequence, sep=", ")
print(*second_sequence, sep=", ")
