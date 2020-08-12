import psycopg2

from passw import dbname, user, password, host #import sensitive info
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

table_create = """
CREATE TABLE titanic (
    id SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name VARCHAR(500),
    Sex VARCHAR(80),
    Age FLOAT(4),
    \"Siblings/Spouses Aboard\" INT,
    \"Parents/Children Aboard\" INT,
    Fare FLOAT(4)
)
"""
pg_curs.execute(table_create)
with open('titanic.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
   
    pg_curs.copy_from(f, 'titanic', sep=',',columns=('Survived','Pclass','Name','Sex','Age',
                                                     '\"Siblings/Spouses Aboard\"',
                                                     '\"Parents/Children Aboard\"','Fare'))

pg_conn.commit()
pg_curs.close()
pg_conn.close()

