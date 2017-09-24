# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 07:41:34 2017

@author: Gabriel
"""

months = 12
balance = 4773
annualInterestRate = 0.2
monthlyPaymentRate = 434.9
monthlyInterestRate = annualInterestRate / 12

while months > 0:
    minimumMonPayment   = monthlyPaymentRate * balance
    monthlyUnpaidBalan  = balance - monthlyPaymentRate
    # Result of the balance
    balance = monthlyUnpaidBalan + (monthlyInterestRate * monthlyUnpaidBalan)
    months -= 1

print('Remaining balance:', format(balance, '.2f'))

