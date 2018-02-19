class Person(object):
    def __init__(self, val):
        self.val = val
        self.index = 0
    def getV(self):
        return self.val
    def setV(self, value):
        self.val = value
