import shelve

def store_person(db):
    pid = raw_input("Enter ID number: ")
    pid = pid.strip().lower()
    person = {}
    person['name'] = raw_input('Enter name: ')
    person['age'] = raw_input('Enter age: ')
    person['sex'] = raw_input('Enter sex: ')
    db[pid] = person

def lookup_person(db):
    pid = raw_input('Enter ID number: ')
    pid = pid.strip().lower()
    field = raw_input('Enter filed (name, age, sex) for the value you want to query: ')
    field = field.strip().lower()
    print field.capitalize() + ": ", db[pid][field]
                    

def help():
    print 'just help'

def command():
    cmd = raw_input("Enter field (? for help): ")
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('db_test')
    try:
        while True:
            cmd = command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__' : main()
