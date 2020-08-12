# Part 1 : transfer sqlite to postgreSQL
# Import Libraries
import sqlite3
import psycopg2
from passw import dbname, user, password, host #import sensitive info
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

#Connect to sqlite db and get files
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
GET_TABLE_INFO = 'SELECT * FROM charactercreator_character'
sl_curs.execute(GET_TABLE_INFO)
characters = sl_curs.fetchall()

#Create postgreSQL table 
create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""

pg_curs.execute(create_character_table)

for character in characters:
      insert_character = """
      INSERT INTO charactercreator_character
      (name,level,exp,hp,strength,intelligence,dexterity,wisdom)
      VALUES """ + str(character[1:]) + ";"
      pg_curs.execute(insert_character)
pg_conn.commit()

# Now the data looks the same but lets check it systematically
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character
pg_curs.close()
sl_curs.close()
pg_conn.close()
sl_conn.close()