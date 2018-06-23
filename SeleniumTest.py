# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 05:49:18 2018

@author: unmanaged 5
"""

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

user = "*********"

pwd = "******"

edge_path = "C://Users//unmanaged 5//Desktop//python code"

driver = webdriver.Edge(edge_path)

driver.get("https://www.facebook.com")

assert "Facebook" in driver.title

elem = driver.find_element_by_id("email")

elem.send_keys(user)

elem = driver.find_element_by_id("pass")

elem.send_keys(pwd)

elem.send_keys(Keys.RETURN)

#driver.close()