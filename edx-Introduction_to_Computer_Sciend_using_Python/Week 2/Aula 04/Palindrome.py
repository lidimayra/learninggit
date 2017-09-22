# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:35:43 2017

@author: Gabriel
"""

def palindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        
        return ans
    
    def iterate(s, a, b):
        if(a >= b):
            return True
        if(s[a] == s[b]):
            return iterate(s, a + 1, b - 1)
        if(s[a] != s[b]):
            return False
    
    s = toChars(s)
    
    if(len(s) == 0):
        return True
    
    return iterate(s, 0, len(s) - 1)
    
print(palindrome('Able was I, ere I saw Elba'))

'''
    Course mode to doing palindrome comparation
'''
def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))

print(isPalindrome('Able was I, ere I saw Elba'))