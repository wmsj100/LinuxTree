class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name

class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return "{} studies {} and is in {} year".format(self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teachers {}".format(self.name, ','.join(self.papers))

p1 = Person('Sachin')
s1 = Student('Kushal', 'CSE', 2005)
t1 = Teacher('Prashad', ['C', 'C++'])

print(p1.get_details())
print(s1.get_details())
print(t1.get_details())
