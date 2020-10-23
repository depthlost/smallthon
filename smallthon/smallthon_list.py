def first(self):
    return self[0]
    
def last(self):
    return self[-1]

def detect(self, function, default=None):
    for each in self:
        if (function(each)):
            return each
    return default

def select(self, function):
    return [ each for each in self if function(each) ]
    