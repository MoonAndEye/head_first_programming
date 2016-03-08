import sqlite3

def find_details(id2find):
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row['id'] == id2find:
            s = {}
            s['id'] = str(row['id'])
            s['name'] = row['name']
            s['average'] = str(row['average'])
            s['board'] = row['board']
            s['age'] = str(row['age'])
            cursor.close()
            return(s)
    cursor.close()
    return({})
    
lookup_id = int(input("Enter the id of the surfer: "))
s = find_details(lookup_id)

if s:
    print ("ID:            " + s['id'])
    print ("Name:          " + s['name'])
    #print ("Country:       " + s['country #不知道為何，country沒東西
    print ("Average:       " + s['average'])
    print ("Board type:    " + s['board'])
    print ("Age:           " + s['age'])