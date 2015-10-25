#!/usr/bin/env python3

# exercise
name = input("What is your name? ")
response = "Hello, {name}, nice to meet you!".format(name=name)
print(response)


# no variables challenge
print("Hello, {name}, nice to meet you!".format(name=input("What is your name? ")))

# different greetings challenge
greeting_default = "Nice to meet you, {name}!"
greeting_map = {
    "Ruben": "{name}! Wow, you've gotten a big beard.",
    "Andrea": "Oh, {name}, I was meaning to pay you back...",
    "Kermit": "{name}, did you know you are called 'Gustavo' in Spain?"
    }

name = input("What is your name? ")
response = greeting_map.get(name, greeting_default)
print(response.format(name=name))
