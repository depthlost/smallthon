def first(self):
    return self[0]
    
def last(self):
    return self[-1]

def add(self, element):
    return self.add_last(element)

def add_first(self, element):
    self.insert(0, element)
    return element

def add_last(self, element):
    self.append(element)
    return element

def size(self):
    return len(self)

def detect(self, function, default=None):
    for each in self:
        if (function(each)):
            return each
    return default

def select(self, function):
    return [ each for each in self if function(each) ]
