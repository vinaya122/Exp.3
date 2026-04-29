# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:30:07 2026

@author: Agce
"""

# Generate multiplication tables from 1 to 10
for i in range(1, 11): # numbers from 1 to 10
    print(f"\nMultiplication Table of {i}:")
    for j in range(1, 11): # multiply from 1 to 10
        print(f"{i} x {j} = {i*j}")