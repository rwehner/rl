'''
Implementation of a tree structure.
Uses recursive composition
'''
class Tree:
    def __init__(self, key, data=None):
        "Create a new Tree object with empty L & R subtrees"
        self.key = key
        self.data = data
        self.left = self.right = None
    def insert(self, key, data=None):
        "Insert a new element into the tree in the correct position"
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Tree(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Tree(key, data)
        else:
            raise ValueError("Attempt to insert duplicate value")

    def walk(self):
        "Generate the keys from the tree in sorted order"
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key
        if self.right:
            for n in self.right.walk():
                yield n 
        
    def find(self, key):
        "Return the data in the node identified by key."
        if key == self.key:
            return self.data
        elif key < self.key:
            if self.left:
                return self.left.find(key)
        elif key > self.key:
            if self.right:
                return self.right.find(key)
        raise KeyError("No key '{!r}' found".format(key))