__metaclass__ = type
class ZeroError(Exception): pass
class Calcu:
    state = True
    def jisuan(self, str):
        try:
            return eval(str)
        except ZeroDivisionError:
            if self.state:
                print 'the secone num cant be zero'
            else:
                raise

class UserInput:
    try:
        x = input('first number: ')
        y = input('second number: ')
        print x/y
    except (ZeroDivisionError, TypeError), e:
        #print 'the secone number cant be zero'
        print e
    print 'asdf'
