import shelve
s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']

