def test(a,b=-99):
    if a > b:
        return True
    else:
        return False
#a = test(1)
#b = test(1,2)
#print(a,b)

def f(a, data=[]):
    data.append(a)
    return data
#print(f(1), f(2))

def func(a, b=5, c=10):
    print(a,b,c)
func(12,24)
func(12, c=24)
func(b=12, c=24, a=-1)
