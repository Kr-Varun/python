# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 03:38:31 2018

@author: unmanaged 5
"""

import requests

#response=requests.get("https://www.quandl.com/api/v3/datasets/NSE/IBULISL.json?api_key=EheeGgpoHs89AdrK6t4w")
#print(response.status_code)

#for obj in response.json():
 #   print(obj)
    

#for obj in response:
   # print(obj)
    

#for i in range(0,7):
 #   print(response.json()["dataset"]["data"][i]) #[0] for just one day, without [0] it would print all the data





response=requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=Pune&destination=Mumbai")
print(response.status_code)
print(response.json()["routes"][0]["legs"])