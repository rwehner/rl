"""
Run the mailJOTD program for various
DAYCOUNTs and output the performance
for each.
"""
import timeit

print('As originally written:')
for DAYCOUNT in [1, 10, 50, 100, 500]:
    setup = """
import mailJOTD
from settings import STARTTIME, RECIPIENTS
DAYCOUNT = %s""" % (DAYCOUNT)

    # Do 10 runs, report the best one
    best = min(timeit.repeat('mailJOTD.main(STARTTIME, DAYCOUNT, RECIPIENTS)',
                             setup=setup, repeat=10, number=1))
    print("daycount={0}\tbesttime={1}\tper_msg={2}".format(DAYCOUNT, round(best, 6), round(best/DAYCOUNT, 6)))

print('\nWith "multi" functions:')    
for DAYCOUNT in [1, 10, 50, 100, 500]:
    setup = """
import mailJOTD
from settings import STARTTIME, RECIPIENTS
DAYCOUNT = %s""" % (DAYCOUNT)

    # Do 10 runs, report the best one
    best_multi = min(timeit.repeat('mailJOTD.main_multi(STARTTIME, DAYCOUNT, RECIPIENTS)',
                             setup=setup, repeat=10, number=1))
    print("daycount={0}\tbesttime={1}\tper_msg={2}".format(DAYCOUNT, round(best_multi,6), round(best_multi/DAYCOUNT,6)))        