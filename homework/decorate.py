#!/usr/bin/env python3

# quick example of decorators to see if I remember


def capit(func, *args):
    def inner(*args):
        s = func(*args)
        return s.upper()
    return inner


@capit
def sayit(message):
    return message

if __name__ == "__main__":
    msg = "This is my message."
    print(sayit(msg))
