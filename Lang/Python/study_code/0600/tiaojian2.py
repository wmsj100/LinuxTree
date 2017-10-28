name = ['ww', 'lisi', 'zhaoliu', 'wmz']
age=[ 12, 32, 34, 52]
for i in range(len(name)):
    print name[i], 'is ', age[i]
for n, a in zip(name, age):
    print n, ' ', a
age.append(54)
for n, a in zip(name, age):
    print n, a
