#   Write a function named math_operations that receives a different number of floats as arguments and 4 keyword
#   arguments. The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
#   You need to take each float argument from the sequence and do mathematical operations as follows:
#   •	The first element should be added to the value of the key "a"
#   •	The second element should be subtracted from the value of the key "s"
#   •	The third element should be divisor to the value of the key "d"
#   •	The fourth element should be multiplied by the value of the key "m"
#   •	Each result should replace the value of the corresponding key
#   •	You must repeat the same steps consecutively until you run out of numbers
#   Beware: You cannot divide by 0. If the operation could throw an error, you should skip the operation and continue
#   to the next one.
#   After you finish calculating all numbers, sort the four elements by their values in descending order. If two or more
#   values are equal, sort them by their keys in ascending order (alphabetically).
#   In the end, return each key-value pair in the format "{key}: {value}" on separate lines. Each value should be
#   formatted to the first decimal point.

def math_operations(*numbers, **operations):
    counter = 1
    for num in numbers:
        if num == 0 and counter == 3:
            counter += 1
            continue

        if counter == 1:
            operations["a"] += num
        elif counter == 2:
            operations["s"] -= num
        elif counter == 3:
            operations["d"] /= num
        elif counter == 4:
            operations["m"] *= num

        counter += 1
        if counter > 4:
            counter = 1

    sorted_operations = sorted(operations.items(), key=lambda x: (-x[1], x[0]))
    result = []
    for el in sorted_operations:
        result.append(f"{el[0]}: {el[1]:.1f}")
    return '\n'.join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))