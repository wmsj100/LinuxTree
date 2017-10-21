while True:
    try:
        x=input('first number: ')
        y = input('second number: ')
        print x/y
    except Exception, e:
        print e
    else:
        break
    finally:
        print 'cleaning up.'
