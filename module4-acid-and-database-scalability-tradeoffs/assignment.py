import pymongo
import psycopg2
from passw import username, password, dbname
from passw import dbname_sql, user_sql , password_sql, host_sql

# Part 1: 

#MONGO DB CONNECT
connecting = "mongodb+srv://"+username+":"+password+"@cluster0.j2uck.mongodb.net/"+dbname+"?retryWrites=true&w=majority"
client = pymongo.MongoClient(connecting)
db = client.test
total_characters = db.test.count_documents({'doc_type':'rpg_character'})
print("Total Number of Characters: ", total_characters)

# Part 2 : Titanic DB
#POSTGRESQL connect with answers 

pg_conn = psycopg2.connect(dbname=dbname_sql, user=user_sql,
                           password=password_sql, host=host_sql)
pg_curs = pg_conn.cursor()

def execute_query(cursor,query):
    cursor.execute(query)
    return cursor.fetchall()

def printer(cursor,result):
    print([i[0] for i in cursor.description])
    for passanger in result:
        print(passanger[:])

survived = execute_query(pg_curs,"SELECT COUNT(*) FROM titanic WHERE Survived = 1")
not_survived = execute_query(pg_curs,"SELECT COUNT(*) FROM titanic WHERE Survived = 0")
passanger_per_class = execute_query(pg_curs,"SELECT pclass AS class, COUNT(*) AS Passangers FROM titanic GROUP BY pclass order by pclass;")

print("Survived: ",survived[0][0])
print("Didn't Survived: ", not_survived[0][0])
print("Passangers Per Class: ")
print("Class  # of Passangers: ")
printer(pg_curs,passanger_per_class)

survived_per_class = execute_query(pg_curs,"SELECT pclass AS class, COUNT(*) AS Passangers_survived FROM titanic WHERE survived = 1 GROUP BY pclass order by pclass;")
print("Survived Per class: ")
printer(pg_curs,survived_per_class)


print("Didn't Survived Per Class")
didnt_surv_pclass = execute_query(pg_curs,"SELECT pclass AS class, COUNT(*) AS Passangers_not_survived FROM titanic WHERE survived = 0 GROUP BY pclass order by pclass;")
printer(pg_curs,didnt_surv_pclass)

#Avg age of survivors vs Non
print("Average Age Survived vs Not Survived: ") 
avg_age_surv_vs_non = execute_query(pg_curs,"SELECT survived, AVG(age) AS average_age FROM titanic GROUP BY survived order by survived;")
printer(pg_curs,avg_age_surv_vs_non)
#avg age each passanger class
print("Average Age Per Class: ")
avg_age_per_class = execute_query(pg_curs,"SELECT pclass AS class, AVG(age) AS average_age FROM titanic GROUP BY pclass order by pclass;")
printer(pg_curs,avg_age_per_class)

#avg fare per class
print("Avergae Fare Per Class")
avg_fare_per_class = execute_query(pg_curs,"SELECT pclass AS class, AVG(Fare) AS average_fare FROM titanic GROUP BY pclass order by pclass;")
printer(pg_curs,avg_fare_per_class)
#avg_per_survival
print("Average fare per Survival")
avg_fare_per_survival = execute_query(pg_curs,"SELECT survived, AVG(Fare) AS average_fare FROM titanic GROUP BY survived order by survived;")
printer(pg_curs,avg_fare_per_survival)

#siblings per class
print("Average Siblings Per Class:")
siblings_per_class = execute_query(pg_curs,"SELECT pclass, CAST(AVG(\"Siblings/Spouses Aboard\") AS FLOAT) AS Siblings_spouses FROM titanic GROUP BY pclass ORDER BY pclass;")
printer(pg_curs,siblings_per_class)

#siblings per survival
print("Average Siblings per Survival: ")
siblings_per_survival = execute_query(pg_curs,"SELECT survived, CAST(AVG(\"Siblings/Spouses Aboard\") AS FLOAT) AS Siblings_spouses FROM titanic GROUP BY survived ORDER BY survived;")
printer(pg_curs,siblings_per_survival)

#average children/parent per class:
print("Average Parent/children per Class: ")
parent_child_per_class = execute_query(pg_curs,"SELECT pclass, AVG(\"Parents/Children Aboard\") AS parents_children FROM titanic GROUP BY pclass ORDER BY pclass;")
printer(pg_curs,parent_child_per_class)
#average parent/children survival
print("Average parent/children per survival")
avg_parent_child_survival = execute_query(pg_curs,"SELECT survived, CAST(AVG(\"Parents/Children Aboard\") AS FLOAT) AS parents_children FROM titanic GROUP BY survived ORDER BY survived;")
printer(pg_curs,avg_parent_child_survival)

# Same Name Passanger

same_name_passger = execute_query(pg_curs,"SELECT COUNT(*) FROM (SELECT COUNT(name) AS n FROM titanic GROUP BY name HAVING COUNT(name) > 1) as t;")
print("Same Name Passsanger: ",same_name_passger[0][0])