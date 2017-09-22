# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 06:37:21 2017

@author: Gabriel
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    Returns True if is in aStr; False otherwise
    '''
    if(len(aStr) <= 1 and aStr != char):
        return False
    
    middle  = int(len(aStr) // 2)
    midChar = aStr[middle]
    
    if(char == midChar):
        return True
    elif(char < midChar):
        return isIn(char, aStr[:middle])
    elif(char > midChar):
        return isIn(char, aStr[middle:])

print(isIn('h', 'abcdefg'))