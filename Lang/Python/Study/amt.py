class Account(object):
    def __init__(self, rate):
        self.rate = rate
        self.__amt = 0

    @property
    def amount(self):
        return self.__amt

    @property
    def cny(self):
        return sefl.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("sorry, nolll")
            return
        self.__amt = value
if __name__ == '__main__':
    acc = Account(rate=6.6)
    acc.amount = 20
    print(acc.amount)
    print(acc.cny)
