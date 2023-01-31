#   You will be given some emails until you receive the command "End". Create the following custom exceptions to
#   validate the emails:
#   · NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in
#     the email "peter@gmail.com")
#   · MustContainAtSymbolError - raise it when there is no "@" in the email
#   · InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
#   When an error is encountered, raise it with an appropriate message:
#   · NameTooShortError - "Name must be more than 4 characters"
#   · MustContainAtSymbolError - "Email must contain @"
#   · InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
#
#   Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
#   If the current email is valid, print "Email is valid" and read the next one

class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LENGTH = 4
valid_domains = ["com", "bg", "org", "net"]

while True:
    email_to_validate = input()
    if email_to_validate == "End":
        break
    name = email_to_validate.split("@")[0]
    domain = email_to_validate.split(".")[-1]
    if "@" not in email_to_validate:
        raise MustContainAtSymbolError("Email must contain @")

    elif len(name) < MIN_NAME_LENGTH:
        raise NameTooShortError(f"Name must be more than {MIN_NAME_LENGTH} characters")

    elif domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print(f"Email {email_to_validate} is valid")



