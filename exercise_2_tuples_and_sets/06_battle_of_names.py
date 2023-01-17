# You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values
# of each letter in the name and integer divide it by the number of the current row (starting from 1).
# Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even.
# After that, sum the values of each set.
#   •	If the sums of the two sets are equal, print the union of the values, separated by ", ".
#   •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
#       separated by ", ".
#   •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values,
#       separated by ", ".
# NOTE: On every operation, the starting set should be the odd set

number_of_names = int(input())
odd_set = set()
even_set = set()
final_set = set()

for row in range(1, number_of_names + 1):
    current_name = input()
    list_of_ascii_values = []
    for char in current_name:
        list_of_ascii_values.append(ord(char))
    final_result = sum(list_of_ascii_values) // row
    if final_result % 2 == 0:
        even_set.add(final_result)
    else:
        odd_set.add(final_result)

if sum(odd_set) == sum(even_set):
    final_set = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    final_set = odd_set.difference(even_set)
elif sum(odd_set) < sum(even_set):
    final_set = odd_set.symmetric_difference(even_set)

print(*final_set, sep=", ")