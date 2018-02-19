girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
wrap = {}
for boy in boys:
    wrap.setdefault(boy[0], []).append(boy)
arr=[b + '+' + g for b in boys for g in wrap[b[0]] ]
