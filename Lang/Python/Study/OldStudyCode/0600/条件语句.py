name = raw_input('please input naem: ')
if name.endswith('wmsj'):
    if name.startswith('mr'):
        print 'hello mr' + name
    elif name.startswith('mrs'):
        print 'hello mrs' + name
    else:
        print 'hello ' + name
elif name.endswith('wanmei'):
    print 'wanmei'
else: print 'others'

