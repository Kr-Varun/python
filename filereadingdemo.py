# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 02:45:29 2018

@author: unmanaged 24
"""

import os
path="C:\\Users\\unmanaged 24\\Desktop\\python_code"

for (dirpath,dirnames,filenames) in os.walk(path):
    #print(filenames)
    #print(dirnames)
    
    for file in filenames:    #array of files in filenames variable
        #print(file)
        
        (filename,extension)=os.path.splitext(file)  #splitting into two variables filename and extension
        #print(filename,"-->",extension)
#        if (extension==".txt"):
#            content=open(path+"\\"+file,'r') #r is for read-only
#            for line in content:
#                print(line)
        
        if (extension==".csv"):
            content1=open(path+"\\"+file,'r') #r is for read-only
            for line1 in content1:
                print(line1)