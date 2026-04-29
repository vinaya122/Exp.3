# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:29:04 2026

@author: Agce
"""

# EMI Calculator
p = float(input("Enter loan amount: "))
r_annual = float(input("Enter annual interest rate: "))
n = int(input("Enter months: "))

# Convert annual rate to monthly decimal
r = r_annual / (12 * 100)

# EMI Formula
emi = (p * r * (1 + r)**n) / ((1 + r)**n - 1)

print("EMI =", round(emi, 2))