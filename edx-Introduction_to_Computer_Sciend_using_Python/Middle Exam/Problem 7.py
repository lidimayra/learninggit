# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:41:20 2017

@author: Gabriel
"""

def score(word, f):
   """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int
   """
   highest = 0
   lower = 0
   for pos in range(len(word)):
       valueA = calculateScore(pos, word[pos].lower())
       if valueA >= highest:
           lower = highest
           highest = valueA
       elif valueA > lower:
           lower = valueA
           
   return f(highest, lower)

def calculateScore(index, letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return  index * (alphabet.index(letter) + 1)

def doSomething(a, b):
    return a + b

print(score('woor', doSomething))