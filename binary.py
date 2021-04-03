# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 08:21:26 2021

@author: hayas
"""

def binary(num):
    if num >= 1:
        binary(num // 2)
    print (num % 2)