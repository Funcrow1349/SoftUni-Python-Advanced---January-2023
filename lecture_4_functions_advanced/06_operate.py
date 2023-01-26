#   Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple
#   numbers (integers) as additional arguments (*args). The function should return the result of the operator applied
#   to all the numbers. For more clarification, see the examples below.
#   Submit only your function in the Judge system.
#   Note: Be careful when you have multiplication and division


def operate(operator, *args):

    def addition():
        result = args[0]
        for num in range(1, len(args)):
            result += args[num]
        return result

    def subtraction():
        result = args[0]
        for num in range(1, len(args)):
            result -= args[num]
        return result

    def multiplication():
        result = args[0]
        for num in range(1, len(args)):
            result *= args[num]
        return result

    def division():
        result = args[0]
        for num in range(1, len(args)):
            result /= args[num]
        return result

    if operator == "+":
        return addition()
    elif operator == "-":
        return subtraction()
    elif operator == "*":
        return multiplication()
    elif operator == "/":
        return division()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 1, 2, 3))