"""
Write a program that creates a ten megabyte data file in 
two different ways, and time each method. The first technique 
should create a memory-mapped file and write the data by setting 
one chunk at a time using successively higher indexes. The second 
technique should create an empty binary file and repeatedly use the 
write() method to write a chunk of data. Show how the timings vary 
with the size of the chunk.
"""
import os
import mmap

def normal_file_writer(fh, chunksize=1024, totalsize=10485760):
    """
    Write out data in chunks of chunksize to a open file object fh until
    it reaches total size. All sizes in bytes.
    """
    for i in range(int(totalsize/chunksize)):
        fh.write(chunksize*b'\0')
            
def mapped_file_writer(fh, chunksize=1024, totalsize=10485760):
    """
    memory-map a an open file object fh, then write out chunks of chunksize until
    it reaches totalsize. All sizes in bytes.
    """
    mapf = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_WRITE)
    offset = 0
    for i in range(int(totalsize/chunksize)):
        mapf[offset:offset+chunksize] = chunksize*b'\0'
        offset += chunksize
    mapf.close()
    
if __name__ == "__main__":
    from timer import Timer

    CHUNKSIZES = (1, 512, 1024, 10240)
    FILENAME = r"V:\workspace\Python4_Homework15\src\tenmb_file"

    with open(FILENAME, 'wb') as f:
        for chunksize in CHUNKSIZES:
            with Timer() as mytimer:
                normal_file_writer(f, chunksize=chunksize)
            print("Normal (chunksize={0} bytes) took {1:.7} sec".format(chunksize, mytimer.elapsed_secs))
            f.truncate(0)
    # create a 10mb file to map
    with open(FILENAME, 'wb') as f:
        normal_file_writer(f)
    
    with open(FILENAME, 'r+b') as f:
        for chunksize in CHUNKSIZES:
            with Timer() as mytimer:
                mapped_file_writer(f, chunksize=chunksize)
            print("Mapped (chunksize={0} bytes) took {1:.7} sec".format(chunksize, mytimer.elapsed_secs))                  
    os.unlink(FILENAME)