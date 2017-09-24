def gcdIter(a, b):
    greatest = 0
    if(a >= b):
        greatest = a
    else:
        greatest = b
    
    def iter(a, b, greatest):
        if(a % greatest == 0 and b % greatest == 0):
            return greatest
        else:
            return iter(a, b, greatest - 1)

    return iter(a, b, greatest)

print(gcdIter(8, 12))

def gcdRecur(a, b):
    if(a == 0):
        return b
    elif(b == 0):
        return a
    else:
        return gcdRecur(b, a % b)
        
print(gcdRecur(24, 15))