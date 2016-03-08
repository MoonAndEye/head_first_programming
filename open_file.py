# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:44:23 2016

@author: Moon
"""
highest_score = 0
result_f = open("results.txt")
scores = {}

for each_line in result_f:
    #print (each_line)
    (name, score) = each_line.split()
    #scores.append(float(score))
    #if float(score) > highest_score:
        #highest_score = float(score)
    scores[score] = name
result_f.close()
#scores.sort(reverse = True)
#scores.reverse()
#a=scores.pop()
print ("The highest score was:")
for each_score in sorted(scores.keys(), reverse = True):
    print ('Surfer ' + scores[each_score] + ' scored ' + each_score)

#print (scores[0])
#print (scores[1])
#print (scores[2])