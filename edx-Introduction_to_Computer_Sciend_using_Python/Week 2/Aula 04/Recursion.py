def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b - 1)
    
print(mult(2, 5))

def factorial(a):
    '''
    a = int or float
    Return a recursive calculus of factorial
    '''
    if(a == 1):
        return 1
    else:
        return a*factorial(a - 1)
    
def iterPower(base, exp):
    result = 1
    while exp > 0:
        result = base * result
        exp -= 1
    
    return result

print(iterPower(0.51, 0))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if(exp == 0):
        return 1
    if(exp == 1):
        return base
    else:
        return base*recurPower(base, exp - 1)

print(recurPower(3.15, 10))

