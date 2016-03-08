# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 12:56:58 2016

@author: Moon
"""
import promotion
import starbuzz

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
price = [1.50, 2.0, 1.80, 1.20]
running = True

while running:
    option = 1
    for choice in items:
        print (str(option) + ". " + choice)
        option = option + 1
    print (str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        new_price = discount(price[choice-1])
        save_transaction(new_price, credit_card, items[choice -1])
"""
這個code不能輸入1到5以外的數字, error message
error message: list index out of range
"""        
    