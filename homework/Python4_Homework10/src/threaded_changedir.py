import os, os.path
import time
import threading

class MyThread(threading.Thread):
    def __init__(self, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
        self.origdir = os.path.abspath(os.curdir)
    def run(self):
        print(self.name, "started in", self.origdir)
        # only 2nd thread changes dir
        if self.name == "Thread-2":
            print(self.name, "changing dir")
            os.chdir('V:\workspace')
        time.sleep(5)
        self.enddir = os.path.abspath(os.curdir)
        print(self.name, "finished in", self.enddir)
        
bgthreads = threading.active_count()
tt = [MyThread() for i in range(3)]
for t in tt:
    t.start()
print("Threads started")    
print("All threads done")