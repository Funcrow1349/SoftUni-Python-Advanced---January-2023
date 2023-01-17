from collections import deque

string_expression = [x for x in input().split()]
numbers = deque()

for char in string_expression:
    if char == "*":
        result = multiply(numbers)
        numbers = deque()
        numbers.append(result)
    elif char == "+":
        pass
    elif char == "-":
        pass
    elif char == "/":
        pass
    else:
        numbers.append(int(char))

print(numbers)