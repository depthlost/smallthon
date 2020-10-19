import inspect
from forbiddenfruit import curse
from smallthon import smallthon_list

def sm_list():
    for each in [func for func in inspect.getmembers(smallthon_list, predicate=inspect.isfunction)]:
        curse(list, each[0], each[1])
