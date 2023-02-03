#   Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0.
#   Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

symbols_to_replace = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as text:
    data = text.readlines()

    for row in range(0, len(data), 2):

        for symbol in symbols_to_replace:
            data[row] = data[row].replace(symbol, "@")

        print(*data[row].split()[::-1], sep=" ")





