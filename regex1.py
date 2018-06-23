# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 23:37:40 2018

@author: unmanaged 5
"""

import re

"""
reg_pattern=r"[A-Z]{5,25}"
pswd=input("Enter a password: ")

result=re.search(reg_pattern,pswd)

if(result):
    print("Match_found")

else:
    print("Match not found")
    
"""

"""
reg_pattern= r"(?=.*[A-Za-z])" #indicates that it should have minimum one character, . means minimum 1 char
# ?= means lookahead assertion, in this case it would say lookahead for min 1 char
pswd=input("Enter a password: ")

result=re.search(reg_pattern,pswd)

if(result):
    print("Match_found")

else:
    print("Match not found")
    
"""
"""
reg_pattern= r"(?=.*[A-Za-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{4,8})" #This regex says minimum 1 special char, min 1 capital letter, min 1 numeric and 4-8 digits required.
pswd=input("Enter a password: ")

result=re.search(reg_pattern,pswd)

if(result):
    print("Match_found")

else:
    print("Match not found")
"""

str="Customer Number : 455345734 , Date: June 22, 2018"
items= re.findall("[0-9]+", str) #findall will extract the matching pattern and will print

print(items)

items= re.findall("[0-9]+.*:.*", str) #this would say start with number, check for anything before and after :
print(items)



str = "yes I said yes I will Yes."
res = re.sub("[yY]es","no", str) #sub will substitute the yes or Yes by no.
print (res)

str="Task to complete elk by 23 July 2018"

res=re.sub("[0-9]{4}","2020",str)

print(res)

