# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 23:49:40 2017

@author: Gabriel
"""

balance = 4773
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
monthlyPaymentLower = balance / 12
monthlyPaymentUpper = (balance * (1 + monthlyInterestRate)**12) / 12.0

lowestPayment = 0
while True:
    lowestPayment = (monthlyPaymentLower + monthlyPaymentUpper) / 2
    
    aux = balance
    for i in range(12):
        monthlyUnpaidBalan  = aux - lowestPayment
        # Result of the balance
        aux = monthlyUnpaidBalan + (monthlyInterestRate * monthlyUnpaidBalan)       
    
    if(monthlyPaymentLower == lowestPayment or monthlyPaymentUpper == lowestPayment):
        break
    elif(aux > 0):
        monthlyPaymentLower = lowestPayment
    elif(aux < 0):
        monthlyPaymentUpper = lowestPayment
    else:
        break
    
print('Lowest Payment:', round(lowestPayment, 2))
    