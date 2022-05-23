#!/usr/bin/env python3
"""
tip_calculator
"""

print("Welcome to the Tip Calculator!!!")
totalBill = input("What was the total bill? $")
tipPercentage = input("What percentage tip would you like to give (10, 12, or 15)? ")
billSplit = input("How many people to split the bill? ")
amount = (float(totalBill) + (float(totalBill) * (float(tipPercentage))/100)) / int(billSplit)
print(f"Each person should pay: ${round(amount, 3)}")
