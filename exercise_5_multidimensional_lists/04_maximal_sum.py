#   Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its
#   elements. There will be no case with two or more 3x3 squares with equal maximal sum.
#   Input
#   •	On the first line, you will receive the rows and columns in the format "{rows} {columns}" –
#       integers in the range [1, 20]
#   •	On the following lines, you will receive each row with its columns - integers, separated by a single space in
#       the range [-20, 20]
#   Output
#   •	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
#   •	On the following 3 lines, print each element of the found sub-matrix, separated by a single space.

rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = {}

for i in range(rows - 2):
    for j in range(columns - 2):
        upper_left, upper_center, upper_right = matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]
        mid_left, mid_center, mid_right = matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]
        lower_left, lower_center, lower_right = matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]
        total_sum = sum([upper_left, upper_center, upper_right,
                        mid_left, mid_center, mid_right,
                        lower_left, lower_center, lower_right])
        if total_sum not in max_sum.keys():
            max_sum[total_sum] = [[upper_left, upper_center, upper_right],
                                  [mid_left, mid_center, mid_right],
                                  [lower_left, lower_center, lower_right]]

max_result = max(max_sum.keys())
print(f"Sum = {max_result}")
for row in max_sum[max_result]:
    print(*row)

