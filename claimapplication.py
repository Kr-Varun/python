# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:22:35 2018

@author: unmanaged 24
"""
from policy_holder import PolicyHolder
from driver import Driver
from vehicle import Vehicle

import datetime

fromDate=datetime.date(2015,1,1) #year,month,day
toDate=datetime.date(2019,1,1)
dob=datetime.date(1978,4,21)
#policyHolderObj=PolicyHolder(34554,fromDate,toDate,"Ajay","Male",dob)

"""
policyHolderObj.setAddress("Pune")
policyHolderObj.setEmailId("abc@abc.com")
policyHolderObj.setPhone(689548645)

#print(policyHolderObj.getPolicyNo())

print(policyHolderObj.getFromDate().strftime("%A,%B,%Y"))  #strftime inbuilt method: conversion of date to string

print(policyHolderObj.getPolicyHolderName(),"-->",policyHolderObj.getFromDate(),"-->",policyHolderObj.getPolicyNo(),"-->",policyHolderObj.getToDate().strftime("%A,%B,%Y"),policyHolderObj.getAddress())

"""

vehicleObj=Vehicle("MH-1-435",5645684,"red")
vehicleObj.setPolicyHolder(PolicyHolder(34554,fromDate,toDate,"Ajay","Male",dob))
vehicleObj.setDriver(Driver(7645684,"Kiran"))

vehicleObj.setPolicyHolder(PolicyHolder(456566,fromDate,toDate,"Sanjay","Male",dob))


print(vehicleObj.getPolicyHolder().getPolicyHolderName(),"--->",vehicleObj.getRegNo())


print(Vehicle.baseRoadTax)  #static variable from vehicle class used directly without object
print(Vehicle.computeTax(4))

print(vehicleObj.getPolicyHolder().generateReminder().strftime("%d/%m/%Y"))