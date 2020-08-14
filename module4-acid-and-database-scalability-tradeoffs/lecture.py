# ACID ACRONYM 
# Atomicity, consistency, isolation, durability 
# Atomicity guarantees that each transaction is treated as single 'unit' which either succeeds completley
# or fails complately. an atomic system must guarantee atomicity in each and every situation, 
# including power failures, errorand crashes. Multiple statement either go together ordont happen at all
#Concistency ensures that a transaction can only bring the datbase from one valid state to another
#maintainining database invariantes: anydata writtern to he database must be valid according to all defined rules
#including constrains, cascades, triggers , and any combination thereof. This prevents database corruption by an illegal
#transaction, but does not guarantee that a transaction is correct. Referential integrityguarantees the 
#Primary key-foreign key reltaionship
#Isolation- Transaction are often executed contcurrently , islatuion ensures that concurrent execution of transaction leave the database 
#in the same state that would have been obtained if the transaction wher executed 
from functools import reduce
#we want the some of squareed value
#(a fairely real statistical task!)

my_list = [1,2,3,4]

#Traduitional (non=mapreduce)
ssv = sum([i**2 for i in my_list])

#that works fine - but what if we had 40 billion numbers?
#we could use a mapreduce approach
#to be clear - this code still run on one computer
#but mapredue paradigm *oould* be distributed more directly

squared_values = map(lambda i: i**2, my_list)
def reduce_sum(x1,x2):
    return x1 + x2

ssv_mapreduce = reduce(reduce_sum,squared_values)

print("sunm of squared traditionl:",ssv)
print("Sum of squred values map reduce:" + str(ssv_mapreduce))
