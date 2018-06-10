# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 22:05:58 2018

@author: unmanaged 24
"""
import datetime

from abc import ABC,abstractmethod

class RenewalReminder(ABC):
    
    @abstractmethod
    def generateReminder():pass


class PolicyHolder:
    
    def __init__(self,pno,fdate,tdate,name,gender,dob):   #self is the current object, similar to this. in java
        #initialization of the objects
        self.__policyNo=pno   #doubleunderscore in prefix means private variable
        #self.policyNo=pno  without doubleunderscore, it is a public variable
        self.__fromDate=fdate
        self.__toDate=tdate
        self.__policyHolderName=name
        self.__gender=gender
        self.__dob=dob
    
    
    def getPolicyNo(self): #getter method to access the private variables outside of class.
        return self.__policyNo
    
    def getFromDate(self):
        return self.__fromDate
    
    def getToDate(self):
        return self.__toDate
    
    def getPolicyHolderName(self):
        return self.__policyHolderName
    
    def generateReminder(self):
        return self.__toDate+ datetime.timedelta(days=10)
    
    def setAddress(self,addr):
        self.__address=addr
    
    def setEmailId(self,email):
        self.__emailId=email
    
    def setPhone(self,phone):
        self.__phoneNo=phone
        
    def getAddress(self):
        return self.__address
    
    def getEmailId(self):
        return self.__emailId
    
    def getPhone(self):
        return self.__phoneNo
#create object
#policyHolderInstance=PolicyHolder(34554,"1/1/2015","1/1/2019","Ajay","Male","21/4/1978")
#print(policyHolderInstance.__policyNo) #policyno is a private variable, so we cannot access this outside class


fromDate=datetime.date(2015,1,1) #year,month,day
toDate=datetime.date(2019,1,1)
dob=datetime.date(1978,4,21)
policyHolderObj=PolicyHolder(34554,fromDate,toDate,"Ajay","Male",dob)

policyHolderObj.setAddress("Pune")
policyHolderObj.setEmailId("abc@abc.com")
policyHolderObj.setPhone(689548645)

#print(policyHolderObj.getPolicyNo())

print(policyHolderObj.getFromDate().strftime("%A,%B,%Y"))  #strftime inbuilt method: conversion of date to string

print(policyHolderObj.getPolicyHolderName(),"-->",policyHolderObj.getFromDate(),"-->",policyHolderObj.getPolicyNo(),"-->",policyHolderObj.getToDate().strftime("%A,%B,%Y"),policyHolderObj.getAddress())