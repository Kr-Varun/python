# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:09:09 2018

@author: unmanaged 24
"""

from driver import Driver
from vehicle import Vehicle,HighEndVehicle,LowEndVehicle



vehicleObj=HighEndVehicle("MH-1-435",5645684,"red",True,True,True)

vehicleObj.setDriver(Driver(7645684,"Kiran"))


#print(vehicleObj.getPolicyHolder().getPolicyHolderName(),"--->",vehicleObj.getRegNo())


print(Vehicle.baseRoadTax)  #static variable from vehicle class used directly without object
print(Vehicle.computeTax(4))

print(vehicleObj.computeTaxByVehicle(2))

vehicleObj=LowEndVehicle("MH-1-435",5645684,"red",True)
print(vehicleObj.computeTaxByVehicle(4))


#upgrading the vehicle
vehicleObj.setABS(True)

#removing airbrake
vehicleObj.setABS(False)