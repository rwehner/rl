"""
control.py: Creates queues, starts output and worker processes,
            and pushes inputs into the input queue.
"""
from random import randrange
from string import ascii_letters

from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread

def randstr(length=1000):
    result = []
    for i in range(length):
        result.append(ascii_letters[randrange(len(ascii_letters))])
    return ''.join(result)

if __name__ == "__main__":
    WORKERS = 10
    
    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))
    
    ot = OutThread(WORKERS, outq)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    instring = randstr()
    # put work on the queue
    for work in enumerate(instring):
        inq.put(work)
    # terminate the process pool
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control process terminating")