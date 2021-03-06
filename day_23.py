import mysql.connector

mydb = mysql.connector.connect(
                            host='localhost',
                            user= 'root',
                            password='password',
                            database='sample_db'
                            )

mycursor = mydb.cursor()


# SELECT statment
mycursor.execute("SELECT * FROM CUSTOMERS")
myresult1 = mycursor.fetchall()

for x in myresult1:
    print(x)


# Customised SELECT statment
mycursor.execute("SELECT age FROM CUSTOMERS WHERE name = 'Trinay'")
myresult2 = mycursor.fetchall()

for x in myresult2:
    print(x)



# Executing a long sql query using Python

qry1 = "SELECT name, age FROM customers WHERE name in ('Dileep', 'Sajana', 'Trinay') ORDER BY 2"

mycursor.execute(qry1)
myresult3 = mycursor.fetchall()

for x in myresult3:
    print(x)



# DELETE statement
# commit() function commits the changes in the actual db. If commit() is not called, the changes wont reflect in the db.

qry2 = "DELETE FROM sample_db.customers WHERE age = 30"
mycursor.execute(qry2)
mydb.commit()
print(mycursor.rowcount, 'record(s) deleted')



# DROP a table: can be done by executing the below query
qry3 = "DROP TABLE customers"


# DROP a table only if it exists
qry4 = "DROP TABLE IF EXISTS customers"


# UPDATE query
qry5 = "UPDATE customers SET age = 4 WHERE name = 'Trinay'"
mycursor.execute(qry5)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")



# JOIN in Python

# Lets create a new table and join to the existing customers table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE relation (age TINYINT(255), relationship VARCHAR(255))")
sql = "INSERT INTO sample_db.relation (age, relationship) VALUES (%s, %s)"
val = [(31, "Self"), (29, "Spouse"), (4, "Son")]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "records were inserted..")


# Lets join both tables using a simple join query.
qry6 = "SELECT c.name, r.relationship \
        FROM customers c\
        JOIN relation r ON c.age = r.age"
mycursor.execute(qry6)

myresult6 = mycursor.fetchall()
for x in myresult6:
    print(x)
