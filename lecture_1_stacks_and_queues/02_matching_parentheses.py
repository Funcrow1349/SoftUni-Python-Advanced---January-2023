# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.

expression = input()
starting_indexes = []

for index in range(len(expression)):
    if expression[index] == "(":
        starting_indexes.append(index)
    elif expression[index] == ")":
        start_index = starting_indexes.pop()
        print(expression[start_index:index + 1])
