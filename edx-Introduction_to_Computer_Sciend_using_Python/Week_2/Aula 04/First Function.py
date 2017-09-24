def is_even( i ):
    '''
    Input: i, a positive int
    Returns True if i is even, otherwise False
    '''
    print('hi')
    return i % 2 == 0

print(is_even(4))

def doSomething(cb):
    return cb()

def a():
    return 2

print(doSomething(a))

def g(x):
    def h():
        x = 'abs'
    
    x = x + 1
    print('in g(x): x = '+ str(x))
    h()
    return x

x = 3
print(g(x))