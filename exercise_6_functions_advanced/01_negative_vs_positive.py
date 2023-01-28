#   You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from
#   the positive. Find the total sum of the negatives and positives, and print the following:
#   •	On the first line, print the sum of the negatives
#   •	On the second line, print the sum of the positives
#   •	On the third line:
#       o	If the absolute negative number is larger than the positive number:
# 	        "The negatives are stronger than the positives"
#       o	If the positive number is larger than the absolute negative number:
# 	        "The positives are stronger than the negatives"
#   Note: you will not receive any zeroes in the input

def sum_negative(nums):
    result = 0
    for num in nums:
        if num < 0:
            result += num
    return result


def sum_positive(nums):
    result = 0
    for num in nums:
        if num > 0:
            result += num
    return result


numbers = [int(x) for x in input().split()]
negatives = sum_negative(numbers)
positives = sum_positive(numbers)
print(negatives)
print(positives)
if abs(negatives) > abs(positives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")



