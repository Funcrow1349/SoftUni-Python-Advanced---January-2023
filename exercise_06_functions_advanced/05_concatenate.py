#   Write a concatenate() function that receives some strings as arguments and some named arguments (the key will be a
#   string, and the value will be another string).
#   First, you should concatenate all arguments successively. Next, take each key successively, and if it is present in
#   the resulted string, change all matching parts with the key's value. In the end, return the final string.
#   See the examples for more clarification.

def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key in kwargs:
        text = text.replace(key, kwargs[key])

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))