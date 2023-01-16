# Write a program that keeps all the unique chemical elements. On the first line, you will be given a number n - the
# count of input lines that you will receive. On the following n lines, you will be receiving chemical compounds
# separated by a single space. Your task is to print all the unique ones on separate lines (the order does not matter)

number_of_elements = int(input())
set_of_elements = set()

for entry in range(number_of_elements):
    current_elements = input().split()
    for element in current_elements:
        set_of_elements.add(element)

for element in set_of_elements:
    print(element)