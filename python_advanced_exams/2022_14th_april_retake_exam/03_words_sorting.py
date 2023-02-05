#   Write a function words_sorting which receives a different number of words.
#   Create a dictionary, which will have as keys the words that the function received. For each key, create a value that
#   is the sum of all ASCII values of that key.
#   Then, sort the dictionary:
#   •	By values in descending order, if the sum of all values of the dictionary is odd
#   •	By keys in ascending order, if the sum of all values of the dictionary is even
#   Note: Submit only the function in the judge system
#   Input
#   •	There will be no input, just any number of words passed to your function
#   Output
#   •	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
#   Constraints:
#   •	There will be no case with capital letters.
#   •	There will be no case with a string consisting of other than letters.

def words_sorting(*words):
    words_dict = {}
    final_result = ""

    for word in words:
        if word not in words_dict:
            words_dict[word] = 0
        for letter in word:
            words_dict[word] += ord(letter)

    total_sum = sum([value for value in words_dict.values()])

    if total_sum % 2 == 0:
        words_dict = dict(sorted(words_dict.items(), key=lambda x: x[0]))
    elif total_sum % 2 != 0:
        words_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1]))

    for key, value in words_dict.items():
        final_result += f"{key} - {value}\n"

    return final_result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))
#
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))
