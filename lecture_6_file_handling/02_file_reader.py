#   You are given a file called numbers.txt with the following content:
#                           1
#                           2
#                           3
#                           4
#                           5
#   Create a program that reads the numbers from the file. Print on the console the sum of those numbers.

with open("numbers.txt") as file:
    total_sum = 0
    for num in file:
        total_sum += int(num)

print(total_sum)

