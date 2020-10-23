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

def reject(self, function):
    return [ each for each in self if not function(each) ]

def collect(self, function):
    return [ function(each) for each in self ]

def do(self, function):
    for each in self: function(each) 

def is_empty(self):
    return self.size() == 0

def flatten(self):
    return [ item for each in self for item in each ]

def remove_duplicated(self):
    result_list = []
    for each in self: 
        if each not in result_list: 
            result_list.append(each)
    return result_list

def flat_collect(self, function):
    return self.collect(function).flatten()

def inject(self, function, initial_value):
    result = initial_value
    for each in self:
        result = function(each, result)
    return result

def includes(self, element):
    return element in self

def any_satisfy(self, function):
    for each in self:
        if function(each):
            return True
    return False

def all_satisfy(self, function):
    for each in self:
        if not function(each):
            return False
    return True