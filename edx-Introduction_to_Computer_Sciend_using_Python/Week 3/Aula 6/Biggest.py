# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:24:11 2017

@author: Gabriel
"""

def biggest(aDict):
    '''
    aDict: a dictionary
    Returns: the key that contains the biggest lenght of values (which key is a list)
    '''
    bigger = ''
    for i in aDict:
        if(bigger == '' or len(aDict[i]) > len(aDict[bigger])):
            bigger = i
    return bigger
