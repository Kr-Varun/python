# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 00:51:08 2018

@author: unmanaged 24
"""

import random 

#print (random.randint(5,10))
"""
#generate 100 customerids

for _ in range(1,100):
    print(random.randint(10000,100000),end="\t")
"""
#to remove duplicates
data=[4,5,6,6,7]
print(set(data))
    
#create list
"""
customerIdList=[]
for _ in range(1,100):
    temp=random.randint(10000,100000)
    customerIdList.append(temp)
    
print(customerIdList)
"""
#or
customerIdList=[]
for _ in range(1,5): # _ means : for that element in that range
    customerIdList.append(random.randint(10000,100000))

#print(customerIdList[50:])
print('Before Sorting')    
print(customerIdList)
customerIdList.sort()
print ("after sorting...")
print(customerIdList)


customerIdList.reverse()
print ("after sorting in reverse...")
print(customerIdList)

"""
#heterogenous data
machineInfo=["172.89.90.91",8080,"PC-1",True,6060,"Port Occupied",7070]

for _ in machineInfo:
    print(type(_))
    if(type(_) is int):
        print((_),end=" ");
    
#print(machineInfo)
        
machineInfo=["172.89.90.91",8080,"PC-1",True,6060,"Port Occupied",7070]
for _ in machineInfo:
   
    if(type(_) is str):
        print("String %s" %(_));
    elif(type(_) is int):
        print(_+100)
    else:
        print(_)
"""

policy=["Policy1","Policy2","Policy3"]
sumInsured=[234876,45378,75873]
years=[4,5,7]
finalList=policy+sumInsured
print(finalList)

#to print corresponding value from each list
for (x,y,z) in zip(policy,sumInsured,years): #zip to concatenate
    print(x,y,z)
    


#list of list
customerList=[[1,"Ajay",576857],[2,"Seema",654948],[3,"Shyam",568766]]
for outer in customerList:
    for inner in outer:
        if(type(inner)is str):
            print(inner)
            
#using position
customerList=[[1,"Ajay",576857],[2,"Seema",654948],[3,"Shyam",568766]]
for outer in customerList:
    if (type(outer[1:2] is str)): #left of colon in 1:2 means include 1st and right of colon means exclude from 2nd element
        print(outer[1:2])