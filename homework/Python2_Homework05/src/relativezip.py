import os
import zipfile

def relativezip(path, zip_fn):
    base = os.path.split(path)[0]
    os.chdir(path)
    files = [os.path.relpath(os.path.abspath(f), base) for f in os.listdir(path) 
             if os.path.isfile(f)]
    os.chdir(base)
    zf = zipfile.ZipFile(zip_fn, 'w')
    for fn in files:
        zf.write(fn)
    zf.close()