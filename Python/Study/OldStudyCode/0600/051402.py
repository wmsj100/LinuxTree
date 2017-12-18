
wrap = {
    'first': {},
    'middle': {},
    'last': {}
    }


def store(data, *fullNames):
    for fullName in fullNames:
        names = fullName.split()
        
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
    
        for label, name in zip(labels, names):
            
            people = data[label].get(name)
            print people, data
            if people:
                if fullName in people:
                    break
                else:
                    people.append(fullName)
            else:
                
                data[label][name] = [fullName]
                #print people, fullName, names, name, label
                #data[label][name] = [fullName]
