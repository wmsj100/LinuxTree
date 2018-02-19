def fn1(path):
    i=0
    tab=0
    space=0
    file = open(path)
    for i, line in enumerate(file):
        space += line.count(' ')
        tab += line.count('\t')
    file.close()
    return space, tab, i+1
print(fn1("String.txt"))
