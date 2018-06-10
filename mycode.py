# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 05:23:38 2018

@author: unmanaged 24
"""
import datetime

holiday=[{"date":"2018-01-26", 
      "holiday":"Republic day"
      },
      {"date":"2018-01-15", 
      "holiday":"Republic day1"
     },
     {"date":"2018-06-10", 
      "holiday":"Republic day2"
     }]


def holidaylist():
    today1=""
    today1=datetime.date.today()
    for each in holiday:
        for(key,value) in each.items():
            if (value==today1):
                for _ in value:
                 print(_)
            

print(holidaylist())
