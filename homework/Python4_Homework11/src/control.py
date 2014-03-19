"""
control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.
"""
from random import randrange
from string import ascii_letters

from queue import Queue
from output import OutThread
from worker import WorkerThread

def randstr(length=1000):
    result = []
    for i in range(length):
        result.append(ascii_letters[randrange(len(ascii_letters))])
    return ''.join(result)

WORKERS = 10

inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS*1.5))

ot = OutThread(WORKERS, outq)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()
instring = randstr()
for work in enumerate(instring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join()
print("Control thread terminating")