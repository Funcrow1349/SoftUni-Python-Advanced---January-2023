#   Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and
#   punctuation marks. The result should be written to another text file.

from string import punctuation

with open("text_task_2.txt", "r") as file:
    sentences = file.readlines()

    with open("output_task_2.txt", "w") as output:
        for i in range(0, len(sentences)):
            letters = 0
            symbols = 0

            for char in sentences[i]:
                if char.isalpha():
                    letters += 1
                elif char in punctuation:
                    symbols += 1

            output.write(f"Line {i+1}: {sentences[i]} ({letters})({symbols})\n")
