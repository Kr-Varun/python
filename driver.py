# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 00:21:50 2018

@author: unmanaged 24
"""

class Driver:
    def __init__(self,licenseNo,name):
        self.__licenseNo=licenseNo
        self.__name=name
        
    def setAddress(self,addr):
        self.__address=addr
    
    def setPhone(self,phone):
        self.__phoneNo=phone
        
    def getAddress(self):
        return self.__address
    
    def getPhone(self):
        return self.__phoneNo