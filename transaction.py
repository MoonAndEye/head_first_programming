# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:41:46 2016

@author: Moon
"""

def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%16s%07d%s/n" % (credit_card, price*100, description))
    file.close()
    