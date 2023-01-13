# You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries.
# Each query is one of these four types:
#   •	'1 {number}' – push the number (integer) into the stack
#   •	'2' – delete the number at the top of the stack
#   •	'3' – print the maximum number in the stack
#   •	'4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
#   "{n}, {n1}, {n2}, ... {nn}"

def push_number(some_number, some_stack):
    some_stack.append(some_number)


def delete_number(some_stack):
    if some_stack:
        some_stack.pop()


def max_number(some_stack):
    if some_stack:
        print(max(some_stack))


def min_number(some_stack):
    if some_stack:
        print(min(some_stack))


number_of_entries = int(input())
stack_of_numbers = []

for entry in range(number_of_entries):
    current_entry = input().split()
    action = current_entry[0]
    if action == "1":
        push_number(int(current_entry[1]), stack_of_numbers)
    elif action == "2":
        delete_number(stack_of_numbers)
    elif action == "3":
        max_number(stack_of_numbers)
    elif action == "4":
        min_number(stack_of_numbers)

stack_of_numbers.reverse()
print(*stack_of_numbers, sep=", ")