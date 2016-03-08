scores = []

highest_score = 0

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split( )
    #print (score)
    score = float (score)
    scores.append(score)
    
    #print (score)
    #if float(score) > float(highest_score):
    #    highest_score = float(score)
    
result_f.close()

scores.sort()
scores.reverse()


print ("The highest score was:")

print (scores[0])    
print (scores[1]) 
print (scores[2]) 