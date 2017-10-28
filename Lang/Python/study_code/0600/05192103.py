def Judeg(obj, val):
    try:
        print obj[val]
    except Exception, e:
        print e
    else:
        print 'has attribute'

a = {
    'q1': 'sss',
    'q2': False
    }
