# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 03:09:09 2018

@author: unmanaged 24
"""

import os
import datetime
import random
path="C:\\Users\\unmanaged 24\\Desktop\\python_code\\logs"


subdirName=input("Enter sub  directory name")

print ("Or like this: " ,datetime.datetime.now().strftime("%H-%M-%S"))

filename="File"+datetime.datetime.now().strftime("%H-%M-%S")+".log"
print(filename)
"""
if (os.path.exists(path)):
    print("directory exists")
    
    
else:
    print("not found")
    dirRef=os.mkdir(path,mode=0o777)  #mode is what permissions to be given to directory, 0o777 means full permissions: 0o: octal, 777:read write access
    if (os.path.exists(path)):
        print("directory exists")
        
"""
        
if (os.path.exists(path)):
    status=True
    
 
else:
   
    dirRef=os.mkdir(path,mode=0o777)  #mode is what permissions to be given to directory, 0o777 means full permissions: 0o: octal, 777:read write access
    status=True

if (status):
    os.mkdir(path+"\\"+subdirName,mode=0o777)
    fileRef=open(path+"\\"+subdirName+"\\"+filename,'a')
    for _ in range (1,100):
        fileRef.write(str(random.randint(100,1000)))
        
    fileRef.close()
