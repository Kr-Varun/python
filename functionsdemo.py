# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 04:27:15 2018

@author: unmanaged 24
"""

#claim settlement

def claimsettlement(amount):
    if (amount<500):
        print("Initiate the fund transfer")
    else:
        amount=amount+200
    return amount
        

print(claimsettlement(700))



import datetime 
def moneytransfer():
    status=""
    currenttime=datetime.datetime.now().hour;
    if (currenttime>20):
        status="fund transfer will happen next day"
    else: 
        status="fund transfer successful"
        
    return status


print(moneytransfer())