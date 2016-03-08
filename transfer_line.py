# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 00:17:58 2016

@author: Moon
"""
"""
line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"

unit = line.split(";")

items =["ID:", "Name:", "Country:", "Average:", "Board type:", "Age:"]

for each in range(len(unit)):
    #print (items[each] + '\t' + unit[each])
    
    
#以下是程式的範,他比較喜歡雜湊 hash
   
s = {}

(s['id'], s['name'], s['country'],s['average'], s['board'], s['age']) = line.split(";")

print ("ID:        " + s['id'])
print ("Name:      " + s['name'])
print ("Country:   " + s['country'])
print ("Average:   " + s['average'])
print ("Board type:" + s['board'])
print ("Age:       " + s['age'])

22102
"""

def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    for each_line in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'],s['average'], s['board'], s['age']) = each_line.split(";")
        if id2find == int(s['id']):
            surfers_f.close()
            return (s)
        surfers_f.close()
    return ([])
 
lookup_id = int(input("Enter the id of the surfer: "))       
s = find_details(lookup_id)

print ("ID:        " + s['id'])
print ("Name:      " + s['name'])
print ("Country:   " + s['country'])
print ("Average:   " + s['average'])
print ("Board type:" + s['board'])
print ("Age:       " + s['age'])