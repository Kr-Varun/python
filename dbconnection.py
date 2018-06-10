# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 05:10:44 2018

@author: unmanaged 24
"""

import pyodbc 

def createConnection():
    conn=pyodbc.connect('DRIVER={SQL SERVER};'
                        'SERVER=DESKTOP-04FB40K;DATABASE=AllstateDB') #connection string contains Db driver,servername,database name,username and password.if using windows authentication, username pwd not required.
    return conn;

def addPolicy(data):
    connObj=createConnection();
    cursor=connObj.cursor();
    print("Cursor ready....");
    try:
        cursor.execute("""insert into Policy values
                       ('%d','%d','%d')""" % (data[0], data[1],data[2]));
        #cursor.execute(query);

        connObj.commit()

    except pyodbc.Error as e:

        print("Exception occurred", e)

        connObj.rollback()
        
testData=[4222,2453453,4274];

addPolicy(testData);        


def getPolicies():
    connObj=createConnection()
    cursor=connObj.cursor();
    cursor.execute("select * from Policy")
    return cursor.fetchall()

for row in getPolicies():
    print(row)
        