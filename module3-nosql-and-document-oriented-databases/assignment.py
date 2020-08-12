
# Working with MongoDB seems easier. However, it is not very organized in my opinion
# Although harder, I prefer SQL. 

import sqlite3
import pymongo
from passw import username,password,dbname

#sqlite Connection

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

curs.execute('SELECT * FROM charactercreator_character')
characters = curs.fetchall() #Fetch all characters
rpg_all_docs_assignment = []

# Transform to json string with extra fields

for character in characters:
    rpg_doc_assignment = {
        'doc_type':'rpg_character',
        'sql_key':character[0],
        'name':character[1],
        'level':character[2],
        'exp':character[3],
        'hp':character[4],
        'strength':character[5],
        'intelligence':character[6],
        'dexterity':character[7],
        'wisdom':character[8]

    }
    rpg_all_docs_assignment.append(rpg_doc_assignment)

print(len(rpg_all_docs_assignment))

#MongoDB Connect

connecting = "mongodb+srv://"+username+":"+password+"@cluster0.j2uck.mongodb.net/"+dbname+"?retryWrites=true&w=majority"
client = pymongo.MongoClient(connecting)
db = client.test

# insert rpg_characters 
# db.test.insert_many(rpg_all_docs_assignment)

printer = list(db.test.find({'doc_type':'rpg_character'}))

#nice print with returns

for printing in printer:
    print(printing)
