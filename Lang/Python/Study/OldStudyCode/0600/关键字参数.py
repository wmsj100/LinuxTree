def hello(name='wmsj', greed='hello', doult='!'):
    return '%s, %s %s' % (greed, name, doult)
def h2(x,y,z=1, *list, **obj):
    print x,y,z
    print list
    print obj

def init():
    labels = ['first', 'middle', 'last']
    return dict.fromkeys(labels, {})

wrap = init()

def lookup(data, lable, name):
    return data[lable].get(name)

def store(data, *fullNames):
    print fullNames
    for fullName in fullNames:
        print fullName
        names = fullName.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = ['first', 'middle', 'last']
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            print people
            if people:
                
                    people.append(fullName)
            else:
                data[label][name] = [fullName]
            
                
                
