#   You will be given two sequences of characters, representing vowels and consonants. Your task is to start checking
#   if the following words could be found:
#   •	"rose"
#   •	"tulip"
#   •	"lotus"
#   •	"daffodil"
#   Start by taking the first character of the vowels collection and the last character from the consonants collection.
#   Then check if these letters are present in one or more of the given words. If a letter is present, that part of the
#   word is considered found. The word is gradually revealed with each letter found. Continue processing the next couple
#   of letters until you find one of the given words above.
#   A letter (vowels or consonants) could participate in more than one word or more than one time in a word, for
#   example:
#   •	The letter "o" is present in "rose", "lotus", and "daffodil".
#   •	The letter "l" is present in "tulip", "lotus", and "daffodil".
#   •	The letter "f" is present in the word "daffodil" twice.
#   The consonant and the vowel are always removed from the collection after trying to match them with the letters in
#   the given words (whether successful or not). In the end, the program stops when a word is found, or there are no
#   more vowels or consonants.
#   As a result, if you found a word, print it and the remaining letters in each collection in the format described
#   below. Otherwise, print "Cannot find any word!" on the first line and the remaining letters in each sequence in the
#   format described below.
#   Look at the provided examples for a better understanding of the problem.
#   Input
#   •	On the first line, you will receive vowels, separated by a single space (" ").
#   •	On the second line, you will receive consonants, separated by a single space (" ").
#   Output
#   •	On the first line:
#       o	If a word is found, print it in the format: "Word found: {word_found}"
#       o	Otherwise, print: "Cannot find any word!"
#   •	On the next lines, print the remaining letters in each collection (if there are any left):
#       o	"Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
#       o	"Consonants left: {consonants_one} {consonants_two} … {consonants_N}"
#   Constraints
#   •	All letters will be lowercase.
#   •	The letter 'y' will always be a vowel.
#   •	The letter 'w' will always be a consonant.

from collections import deque

vowel_sequence = deque(input().split())
consonant_sequence = deque(input().split())
flowers_dict = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

word_found = False

while vowel_sequence and consonant_sequence and not word_found:
    current_vowel = vowel_sequence.popleft()
    current_consonant = consonant_sequence.pop()
    for flower in flowers_dict.keys():
        flowers_dict[flower] = flowers_dict[flower].replace(current_vowel, "")
        flowers_dict[flower] = flowers_dict[flower].replace(current_consonant, "")

        if flowers_dict[flower] == "":
            print(f"Word found: {flower}")
            word_found = True
            break

if not word_found:
    print("Cannot find any word!")

if vowel_sequence:
    print(f"Vowels left: {' '.join(vowel_sequence)}")
if consonant_sequence:
    print(f"Consonants left: {' '.join(consonant_sequence)}")