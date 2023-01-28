#  Write a program that receives a text on the first line and times (to repeat the text) that must be an integer. If the
#  user passes a non-integer type for the times variable, handle the exception and print a message "Variable times must
#  be an integer".

def repeat_text(text, times):
    return text * times


try:
    text_to_repeat = input()
    number = int(input())
    print(repeat_text(text_to_repeat, number))

except ValueError:
    print("Variable times must be an integer")
