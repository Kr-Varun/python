# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 23:56:52 2018

@author: unmanaged 24
"""

orgName="Allstate Solutions Private Ltd."
#slicing
print(orgName[5:9]) #print 5th to 9th character
print(orgName[:-5]) #omitting last 5 characters
print (type(orgName))
print (orgName[2:]) #start from 2nd character

#capitalize method
city="pune"
print(city.capitalize())  #first letter of first word will be shown as capital letter

#padding

#center padding
country="India!"
print(country.center(len(country)+40,"*")) 

#left padding
amount="56857689"
print(amount.ljust(len(amount)+10,"*"))
#right padding
print(amount.rjust(len(amount)+10,"*"))

#reverse string
print(country[::-1])

#encoding and decoding
seqNo=534
import base64
pnrNo=base64.b64encode(str(seqNo).encode(encoding='utf-8',errors='strict'))
print(pnrNo)
print(type(pnrNo))

#for loop
for elem in pnrNo[0:]:  # : is needed in for loop
    print(chr(int(elem)), end="") #end means it would end there and won't go to new line
    print(chr(int(elem)), end="\t")

#decoding
import base64
seqNo=base64.b64decode(bytes(pnrNo).decode(encoding='utf-8',errors='strict'))
print(seqNo)

#or

originalData=base64.b64decode(pnrNo)