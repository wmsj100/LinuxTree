def init(data):
    'init name'
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
    return data
storage = {}
init(storage)

def lookup(data, label, name):
    return data[label].get(name)

def store(data, fullName):
    names = fullName.split();
    labels = ['first', 'middle', 'last']
    if len(names) == 2: names.insert(1, '')
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            if fullName in people:
                break
            else:
                people.append(fullName)
        else:
            data[label][name] = [fullName]
