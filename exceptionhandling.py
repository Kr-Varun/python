# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:45:15 2018

@author: unmanaged 5
"""

class Error(Exception):
    pass

class PwdLengthTooSmall():
    pass

class PwdLengthTooLarge():
    pass

count=0
while (count<=3):
    pwd= input("Enter a password")
    
    try:
        
        if (len(pwd)<4):
            raise PwdLengthTooSmall
        if (len(pwd)>8):
            raise PwdLengthTooLarge
        if ((len(pwd)>4) and len((pwd)<8)):
            break
    
    except PwdLengthTooSmall:
        print("Password is too small")
    except PwdLengthTooLarge:
        print("Password is too large")
    count=count+1