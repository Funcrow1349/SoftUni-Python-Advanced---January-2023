#   Create a program that will receive commands until the command "End". The commands can be:
#   •	"Create-{file_name}" - Creates the given file with an empty content. If the file already exists, remove the
#       existing text in it (as if the file is created again)
#   •	"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it,
#       and add the content
#   •	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old
#       string with the new string. If the file does not exist, print: "An error occurred"
#   •	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"

import os

while True:
    command, *data = input().split("-")
    if command == "End":
        break

    if command == "Create":
        file = open(f"{data[0]}", "w")
        file.close()

    elif command == "Add":
        file = open(f"{data[0]}", "a")
        file.write(f"{data[1]}\n")
        file.close()

    elif command == "Replace":
        try:
            with open(f"{data[0]}", "r+") as file:
                text = file.read()
                file.write(text.replace(data[1], data[2]))
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"{data[0]}")
        except FileNotFoundError:
            print("An error occurred")
