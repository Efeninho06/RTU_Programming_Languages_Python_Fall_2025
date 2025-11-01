"""
Task 2 – Greeting Function with String Manipulation
--------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""


def greet_user(name):
    """return greeting message after cleaning the name"""
    name = name.strip()
    name = name.capitalize()
    message = "Hello, " + name + "! Welcome to Python!"
    return message


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
