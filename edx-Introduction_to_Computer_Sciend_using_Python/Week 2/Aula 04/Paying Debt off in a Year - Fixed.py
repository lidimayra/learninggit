# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 23:16:35 2017

@author: Gabriel
"""

balance = 3926
lowestPayed = 0.01
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
while True:
    aux = balance
    for i in range(12):
        monthlyUnpaidBalan  = aux - lowestPayed
        # Result of the balance
        aux = monthlyUnpaidBalan + (monthlyInterestRate * monthlyUnpaidBalan)       
    
    if(aux > 0):
        lowestPayed += 0.01
    else:
        break
    
    
print('Lowest Payment:', lowestPayed)