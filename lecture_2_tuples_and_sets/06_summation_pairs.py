# On the first line, you will receive a sequence of numbers separated by space. On the second line, you'll receive a
# target number. Your task is to find the pairs of numbers whose sum equals the target number. For each found pair
# print "{number} + {number} = {target_number}". You may NOT use the same element twice to fulfill the condition above.

all_numbers = [int(x) for x in input().split()]
target_number = int(input())

for i in range(len(all_numbers)):
    if all_numbers[i] == "":
        continue
    for j in range(i + 1, len(all_numbers)):
        if all_numbers[j] == "":
            continue
        if all_numbers[i] + all_numbers[j] == target_number:
            print(f"{all_numbers[i]} + {all_numbers[j]} = {target_number}")
            all_numbers[i] = ""
            all_numbers[j] = ""
            break

