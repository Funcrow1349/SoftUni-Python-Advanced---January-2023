#   Write a function called get_info that receives a name, an age, and a town and returns a string in the format:
#   "This is {name} from {town} and he is {age} years old". Use dictionary unpacking when testing your function.
#   Submit only the function in the judge system.


def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
print(get_info(**{"name": "Koko", "town": "Dimitrovgrad", "age": 2}))