#!/usr/bin/env python3


default_greeting = "Hello, {name}, nice to meet you!"
custom_greetings = {
    "Ruben": "{name}! Hola amigo.",
    "Andrea": "Oh, {name}, I was meaning to pay you back...",
    "Kermit": "{name}, did you know you are called 'Gustavo' in Spain?"
    }


def get_name():
    return input("What is your name? ")


def say_hello_primary(default=default_greeting, name_func=get_name):
    ''' basic exercise '''
    name = name_func()
    return default_greeting.format(name=name)


def say_hello_no_variables(default=default_greeting, name_func=get_name):
    '''Challenge: don't use variables
       Let's pretend that making it a testable funcion didn't
       introduce any variables. ;-)
    '''
    return default_greeting.format(name=name_func())


def say_hello_custom_greetings(default=default_greeting,
                               custom_greetings={}, name_func=get_name):
    '''Challenge: use customized greetings for some'''
    name = name_func()
    response = custom_greetings.get(name, default)
    return response.format(name=name)

if __name__ == "__main__":
    print(say_hello_primary())
    print(say_hello_no_variables())
    print(say_hello_custom_greetings(custom_greetings=custom_greetings))
