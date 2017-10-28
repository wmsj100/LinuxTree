__metaclass__ = type

class Tectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError

class Fibs:
    def __init__(self):
        self.a= 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100: raise StopIteration
        return self.a
    def __iter__(self):
        return self

arr = [[1,2], [3,4,5], [5,6]]

def flatten(args):
    for sublist in args:
        for element in sublist:
            yield element

iterator = ((i+1)**2 for i in range(2, 27))

arr1 = [[12,3], 3,4,'sdf', ['asdf', 4, [5,6,]]]
def flatten2(args):
    try:
        try:
            args + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in args:
             for element in flatten2(sublist):
                 yield element
    except TypeError:
        yield args

def flatten3(args):
    try:
        try:
            args + ''
        except TypeError: pass
        else:
            raise TypeError
        for sublist in args:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        yield args


def repeater(val):
    while True:
        new = (yield val)
        if new is not None: val = new

def flatten4(args):
    result = []
    try:
        try:
            args + ''
        except TypeError: pass
        else:
            raise TypeError
        for sublist in args:
            for element in flatten4(sublist):
                result.append(element)
    except TypeError:
        result.append(args)

    return result
