__metaclass__  = type
class Filter:
    def init(self):
        self.block = []
    def find(self, arr):
        return [x for x in arr if x not in self.block]

w=['wmsj', 'haha', 'span']

class newFilter(Filter):
    def init(self):
        self.block = ['span']

class Talk:
    def say(self):
        return self.data
    def haha(self):
        return 'haha'

class Write:
    def pen(self, val):
        self.data = eval(val)
    def haha(self):
        return 'nana'

class Jsj(Talk, Write):
    pass
