# You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number
# in the format "{number} - {count} times". The number must be formatted to the first decimal point.

numbers = tuple([float(x) for x in input().split()])
occurrences = {}
for number in numbers:
    if number not in occurrences.keys():
        occurrences[number] = 0
    occurrences[number] += 1

for key, value in occurrences.items():
    print(f"{key} - {value} times")