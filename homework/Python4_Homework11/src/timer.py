from timeit import timeit

mytime = timeit("import control", number=1)
print("\nThis run took", mytime, "seconds")