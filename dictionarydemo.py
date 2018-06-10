# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 03:12:44 2018

@author: unmanaged 24
"""

#dictionary can be created with {}brackets

user={"id": 1, "name": "Garima", "username": "garry", "email": "abc@abc.com"}

"""
print(user)
print(user.keys())
print(user.values())
print(user["email"]) #to print value of a particular key

for (key,value) in user.items():
    print(key,"==>", value)
"""

#complexity1

user={"id": 1, "name": "Garima", "username": "garry", "email": ["abc@abc.com","cde@cde.com"],
      "skillset":["java","python","c++"]}

for (key,value) in user.items():
    if (key=="name"):
        print(value,end="\t")
    if(key=="skillset"):
        for skill in value: #skill is each element of skillset list, similar to adding (_)
            print (skill,end=",")

#to eliminate , after last skill
for (key,value) in user.items():
    if (key=="name"):
        print(value,end="\t")
    if(key=="skillset"):
        length=len(value)
        count=0
        for _ in value: #skill is each element of skillset list, similar to adding (_)
            if (count<length-1):
                print(_,end=",")
                count=count+1
            else:
                print(_)
                

#complexity2
                
users=[{"id": 1, 
      "name": "Garima", 
      "username": "garry", 
      "email": ["abc@abc.com","cde@cde.com"],
      "skillset":["java","python","c++"]
      },
    {
     "id": 2, 
      "name": "verma", 
      "username": "garry1", 
      "email": ["cde@cde.com"],
      "skillset":["java","python"]
     }
]

for user in users:
    for (key,value) in user.items():
        if (key=="name"):
            print(value,end="\t")
        if(key=="skillset"):
            length=len(value)
            count=0
            for _ in value: #skill is each element of skillset list, similar to adding (_)
                if (count<length-1):
                    print(_,end=",")
                count=count+1
            else:
                print(_)

     