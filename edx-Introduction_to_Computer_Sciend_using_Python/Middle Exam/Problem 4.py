# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:22:56 2017

@author: Gabriel
"""

def getSublists(L, n):
    sublists = []
    lastPos = 0
    total = len(L)
    while total - lastPos >= n:
        sublists.append(L[lastPos:lastPos + n])
        lastPos += 1
    return sublists
   