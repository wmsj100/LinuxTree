__metaclass__ = type
class People:
    num = 0
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def greet(self):
        return 'hello, ' + self.name
    def __haha(self):
        self.name += 'hello '
    def na(self):
        
        self.__haha()
    def init(self):
        People.num += 1

class Filter:
    def init(self):
        self.block = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.block]

class NewFilter(Filter):
    def init(self):
        self.block = ['span']
