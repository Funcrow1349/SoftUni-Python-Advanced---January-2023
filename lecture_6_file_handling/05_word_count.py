#   Write a program that reads a list of words from the file words.txt and finds how many times each of the words is
#   contained in another file text.txt. Matching should be case-insensitive.
#   The results should be written to other text files. Sort the words by frequency in descending order.

with open("words.txt") as words_to_search:
    words = words_to_search.read().split()
with open("input.txt") as input_data:
    text = input_data.read().lower().split()

elements = []

for el in text:
    elements.append("".join(x for x in el if x.isalpha()))

found_elements = {}

for word in words:
    match_counter = 0
    for element in elements:
        if element == word:
            match_counter += 1
        found_elements[word] = match_counter

all_matches = list(sorted(found_elements.items(), key=lambda x: -x[1]))
with open("output.txt", "w") as file:
    for match in all_matches:
        file.write(f"{match[0]} - {match[1]}\n")