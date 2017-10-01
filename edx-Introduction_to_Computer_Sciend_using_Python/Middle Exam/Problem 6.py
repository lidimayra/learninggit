# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:29:11 2017

@author: Gabriel
"""

def flatten(aList):
    newList = {}
    complement(newList, aList)
    return newList
    
def complement(newList, aList):
    for value in aList:
        if(type(value) == list):
            complement(newList, value)
        else:
            newList.append(value)
            
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
