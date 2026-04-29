# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:23:31 2026

@author: Agce
"""

# Nested loops for shop system
for i in range(3): # Outer loop for 3 receipts
    print("Receipt", i + 1)
    for j in range(5): # Inner loop for 5 items per receipt
        print("Item", j + 1)