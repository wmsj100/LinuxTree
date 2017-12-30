counts = int(input("Enter the student's count: "))
data = {}
course = {"math", 'physics', "History"}
for x in range(counts):
    sName = input("Enter the student's name {}: ".format(x+1))
    marks = []
    info = dict()
    for cours in course:
        mark = int(input("Enter the mark of {}: ".format(cours)))
        marks.append(mark)
        info[cours] = mark
    data.setdefault(sName, {'info': info, 'mark': marks})
print(data)
for x,y in data.items():
    for z in y.items():
        z=dict((z,))
        if z.get('mark', 0) != 0:
            val = sum(z['mark'])
            if val > 120:
                print("wawawa {} is beautiful, data is {}, sum is {}".format(x,y['info'], val))
            else:
                print("sorry {} is fail".format(x))
