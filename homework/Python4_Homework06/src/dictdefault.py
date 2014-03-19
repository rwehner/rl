class DictDefault(dict):
    def __init__(self, default):
        self.default = default
        dict.__init__(self)
        
    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default