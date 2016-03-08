#line = "101;Jonny 'wave-boy' Jones;USA;8.32;Fish;21"
import db_app
# We want ID, Name, Country, Average, Board type, Age



#(s['ID'], s['Name'], s['Country'], s['Average'], s['Board type'], s['Age']) = line.split(';')


def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    
    for each_line in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = each_line.split(';')
        if id2find == int(s['id']):
            surfers_f.close()
            return(s)
        
    surfers_f.close()
    return({})
    

lookup_id = int(input("Enter the id of the surfer: "))
s = find_details(lookup_id)

if s:
    print ("ID:            " + s['id'])
    print ("Name:          " + s['name'])
    print ("Country:       " + s['country'])
    print ("Average:       " + s['average'])
    print ("Board type:    " + s['board'])
    print ("Age:           " + s['age'])
    