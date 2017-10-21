__metaclass__ = type

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

class Myclass:
    @staticmethod
    def smth():
        print 'static method'

    @classmethod
    def cmth(cls):
        print 'clas method', cls
