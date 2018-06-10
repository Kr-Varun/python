# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#print statement
print("Welcome to Python....")

#identifiers
firstName="Garima"
lastName="Gupta"
#parameters
print("First Name=%s\nLast Name=%s" %(firstName,lastName))

"""
#input from users
address=input("Enter Address")
print("Address=%s" %(address))  #%s for string
"""

#check the type
print(type(firstName))

"""
#read age
#age=input("Enter Age ")
#print(type(age))

#conversion of datatype
age=int(input("enter age "))
print(type(age))
print("Age=%d " %(age))    #%d for int
"""

#conversion int to hex
memoryAddress=255
hexMemoryAddress=hex(memoryAddress)
print(hexMemoryAddress)
print("Memory Address in hex= %X " %(memoryAddress)) #%X for hexadecimal
#one way of conversion is 38-39 and direct way is 40.


#binary to int conversion
intData=int('100010',2) #2 is the base
print("Interger is =%d" %(intData))
#either above or below can be used
print(int('100010',2))

#int to binary
print(bin(45))

#octal conversion
print(oct(75))

#complex number conversion
real=67
imaginary=56
print(complex(real,imaginary)) #complex number consists of real +imaginary number

#current date using library
from datetime import date
print (date.today())
