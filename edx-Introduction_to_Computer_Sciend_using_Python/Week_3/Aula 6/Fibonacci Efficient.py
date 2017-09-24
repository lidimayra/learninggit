# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:29:52 2017

@author: Gabriel
"""

def fib_efficient(n, d):
    '''
    n: a fibonacci number to be calculated
    d: a dictionary
    '''
    global numFibs
    numFibs += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = ans
        return ans
    
numFibs = 0
    
d = { 1:1, 2:2 }
print(fib_efficient(5, d))

print('Num fibs %s' % (numFibs))

print(fib_efficient(5, d))

print('Num fibs %s' % (numFibs))

print(fib_efficient(35, d))

print('Num fibs %s' % (numFibs))

print(fib_efficient(34, d))

print('Num fibs %s' % (numFibs))


