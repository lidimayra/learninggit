def sum(a = 0, b = 0):
    print(a, b)
    return a + b

print(sum(b = 2, a = 3))

def fourthPower(x):
    '''
    x: int or float.
    '''
    def square(x):
        return x**2
    return square(square(x))

print(fourthPower(2))