# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import unittest
import sys
sys.path.append("C:\\Users\\unmanaged 5\\Desktop\\python code")
from finance import addTax
from finance import calculateDiscount

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_positive_addTax(self): #positive test
        self.assertEqual( addTax(46985,2), 47924.700000000004)
 
    def test_negative_addTax(self): #negative assertion
        self.assertNotEquals( addTax(46985,2), 47690.700000000004)
 
    def test_positive_calculateDiscount(self):
        price=46985
        self.assertTrue(calculateDiscount(46985,2)<price)
        
        
if __name__ == '__main__':
    unittest.main()