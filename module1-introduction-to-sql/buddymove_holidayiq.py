import pandas as pd
import sqlite3
#Part 2

db = pd.read_csv('buddymove_holidayiq.csv')
print(db.shape)
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

db.to_sql('buddymove_holidayiq',conn, if_exists='replace')

QUERY = 'SELECT COUNT(*) FROM buddymove_holidayiq;'

curs.execute(QUERY)
db_sql = curs.fetchall()
print(f'Number of rows in database: {db_sql[0][0]}')
reviews_more_100 = 'SELECT COUNT(*) FROM buddymove_holidayiq WHERE Nature > 100 AND Shopping > 100;'
curs.execute(reviews_more_100)
reviews = curs.fetchall()
print(f'Number of users where reviews of Nature and Shopping more than 100: {reviews[0][0]}')

AVGS = 'SELECT AVG(Sports) , AVG(Religious), AVG(Nature), \
AVG(Theatre),AVG(Shopping), AVG(Picnic) FROM buddymove_holidayiq;'

curs.execute(AVGS)
averages = curs.fetchall()
print(f"average Sports: {averages[0][0]}")
print(f"Average Religious {averages[0][1]}")
print(f"average Nature: {averages[0][2]}")
print(f"Average Theatre: {averages[0][3]}")
print(f"Average Shipping {averages[0][4]}")
print(f"Average Picnic: {averages[0][5]}")
