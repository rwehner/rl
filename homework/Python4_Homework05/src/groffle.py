""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log 
from timeit import Timer 

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

def groffle_faster1(mass, density): 
    total = 0.0 
    masslog = log(mass * density)
    for i in range(10000): 
        total += masslog/(i+1)

    return total

def groffle_faster2(mass, density): 
    masslog = log(mass * density)
    return sum([masslog/(i+1) for i in range(10000)])

def groffle_faster3(mass, density): 
    masslog = log(mass * density)
    return sum(map(masslog.__truediv__, range(1,10001)))
    
if __name__ == "__main__":
    mass = 2.5 
    density = 12.0
    
#    for func in ["groffle_slow", "groffle_faster1", "groffle_faster2", "groffle_faster3"]:
    for func in ["groffle_slow", "groffle_faster3"]:
        timer = Timer("total = {0}(mass, density)".format(func),
                      "from __main__ import {0}, mass, density".format(func)) 
        print("{0} time:".format(func), timer.timeit(number=1000)) 