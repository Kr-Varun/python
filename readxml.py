# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 01:23:24 2018

@author: unmanaged 5
"""

from xml.dom import minidom

doc=minidom.parse("policydata.xml")

policies=doc.getElementsByTagName("Policy")

for policy in policies:
    print(policy.getAttribute("No")) #'No' is the attribute of policy and not the element
    print(policy.getElementsByTagName("PolicyHolderName")[0].firstChild.data) #firstchild is the keyword