#   Patricia wants to go on vacation for the weekend and wants to know where the weather will be the best, so she can
#   see the most sights. Patricia is busy at work and doesn't have time to think about the perfect place for her
#   vacation, so she wants your help.
#   Write a function called forecast that stores information about the weather, and returns sorted information for all
#   locations. The function will receive a different number of arguments. The arguments will be passed as tuples with
#   two elements - the first one is the location, and the second one is the weather:
#   •	Location name: string
#       o	any string
#   •	Weather: string
#       o	"Sunny"
#       o	"Rainy"
#       o	"Cloudy"
#   First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations
#   with cloudy weather, and last are the locations with rainy weather. For each sequence of locations
#   (e.g. all sunny locations), sort them by their name in ascending order (alphabetically).

def forecast(*weather_data):
    final_message = ""
    locations = sorted(weather_data, key=lambda x: ((x[1] == "Rainy"), (x[1] == "Cloudy"), (x[1] == "Sunny"), x[0]))
    for l in locations:
        final_message += f"{l[0]} - {l[1]}\n"
    return final_message


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))

