from timeit import timeit
from random import random

def lst_onemillion(size=1000000):
    return [random() for x in range(size)]

def gen_onemillion(size=1000000):
    return (random() for x in range(size))

print("list() function with list:")
print(timeit("list(lst_onemillion())","from __main__ import lst_onemillion", number=1))

print("list comprehension with list:")
print(timeit("[x for x in lst_onemillion()]","from __main__ import lst_onemillion", number=1))

print("list() function with generator:")
print(timeit("list(gen_onemillion())","from __main__ import gen_onemillion", number=1))

print("list comprehension with generator:")
print(timeit("[x for x in gen_onemillion()]","from __main__ import gen_onemillion", number=1))