"""
worker.py: worker process that receives input through
           one Queue and routes output through another.
"""
from multiprocessing import Process
import sys

class WorkerThread(Process):
    def __init__(self, iq, oq, *args, **kw):
        "init process and get queue refs"
        Process.__init__(self, *args, **kw)
        self.iq, self.oq = iq, oq
    def run(self):
        while True:
            work = self.iq.get()
            if work is None:
                self.oq.put(None)
                print("Worker", self.name, "done")
                self.iq.task_done()
                break
            i, c = work
            result = (i, self.process(c))
            self.oq.put(result)
            self.iq.task_done()
        sys.stdout.flush()
    def process(self, s):
        "defines how string will be processed"
        return s.upper()