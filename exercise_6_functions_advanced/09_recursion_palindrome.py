#   Write a recursive function called palindrome() that will receive a word and an index (always 0). Implement the
#   function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if
#   the word is not a palindrome using recursion.

def palindrome(word, left_index, right_index=-1):
    if left_index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[left_index] != word[right_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, left_index + 1, right_index - 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))