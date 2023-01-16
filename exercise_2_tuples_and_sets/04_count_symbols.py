# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.

def create_set(some_phrase):
    dict_of_symbols = {}
    for x in some_phrase:
        if x not in dict_of_symbols.keys():
            dict_of_symbols[x] = 0
        dict_of_symbols[x] += 1
    return dict_of_symbols


def print_func(symbols_dict):
    for symbol in sorted(symbols_dict.keys()):
        print(f"{symbol}: {symbols_dict[symbol]} time/s")


phrase = input()
symbols = create_set(phrase)
print_func(symbols)


