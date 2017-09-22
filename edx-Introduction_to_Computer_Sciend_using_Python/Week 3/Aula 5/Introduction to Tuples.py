# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:24:48 2017

@author: Gabriel
"""
def oddTuples(aTup):
    '''
    aTup: a Tuple
    
    returns: tuple, every other element of aTup
    '''
    return aTup[::2]

print(oddTuples((2,)))
