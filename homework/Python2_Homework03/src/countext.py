"""
Examine the contests of CWD and print out how may files
of each extension are there.
"""
import glob
import os

def countext():
    files = glob.glob('*')
    extensions = {}
    for file in files:
        name, ext = os.path.splitext(file)
        extensions[ext] = extensions.get(ext, 0) + 1
    return [i for i in extensions.items()]

def printextcount():
    pwd = os.path.abspath(os.path.curdir)
    extensions = countext()
    if not extensions:
        print("No files in %s" % pwd)
        return
    extensions.sort(key=lambda item: item[1], reverse=True)
    print("In %s:" % pwd)
    print('Ext \tCount')
    print('----\t-----')
    for ext in extensions:
        if ext[0] == '':
            ext = ('<none>', ext[1])
        print("%s\t%s" % ext)
        
if __name__ == "__main__":
    printextcount()