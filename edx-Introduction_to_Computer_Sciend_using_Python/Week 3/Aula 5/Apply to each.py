# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 07:38:44 2017

@author: Gabriel
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]

def divideByTwo(value):
    return value / 2

applyToEach(testList, divideByTwo)

print(testList)