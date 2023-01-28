#   Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The
#   command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.

def even_odd(*args):
    command = args[-1]
    result = []
    if command == "even":
        result += [args[i] for i in range(len(args) - 1) if args[i] % 2 == 0]
    else:
        result += [args[i] for i in range(len(args) - 1) if args[i] % 2 != 0]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))