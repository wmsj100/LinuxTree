__metaclass__ = type
class Foobar:
    def __init__(self, value=42):
        self.val = value


class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'hahahaha'
            self.hungry = False
        else:
            print 'no, Im full'

class songBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'squawk'
    def sing(self):
        print self.sound

class girlBird(Bird):
    def __init__(self):
        super(girlBird, self).__init__()    #super lei
        self.sound = 'just sing....'
    def sing(self):
        print self.sound

def checkIndex(key):
    '''
just check key for user input
'''
    if not isinstance(key, (int, long)): raise TypeError
    if key < 0 : raise IndexError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        'chu shi hua suan shu xulie'
        self.start = start
        self.step = step
        self.change = {}

    def __getitem__(self, key):
        'get an item from list'
        checkIndex(key)
        try:
            return self.change[key]
        except KeyError:
            return self.start + self.step * key

    def __setitem__(self, key, value):
        'set an item to list'
        checkIndex(key)
        self.change[key] = value
