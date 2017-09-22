# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:11:59 2017

@author: Gabriel
"""

def keysWithValue(aDict, target):
    keysSorted = []
    
    for key in aDict:
        if(aDict[key] == target):
            keysSorted.append(key)
            
    keysSorted.sort()   
    return keysSorted 

print(keysWithValue({1:1, 2:2, 3:3, 5:3}, 3))