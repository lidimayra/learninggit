# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:16:46 2017

@author: Gabriel
"""
def how_many(aDict):
    '''
    aDict: a dictonary
    Returns: number of elements
    '''
    total = 0
    for pos in aDict:
        total += len(aDict[pos]) 
    return total