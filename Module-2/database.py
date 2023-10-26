import sqlite3

# Database Create/connect
try:
    db = sqlite3.connect("hellodb.db")
    print("Database Connected.")
except Exception as e:
    print(e)

# Create Table

tbl_create = "create table studinfo(id integer primary key autoincrement, name text, sub text)"
try:
    db.execute(tbl_create)
    print("Table Created Successfully!")
except Exception as e:
    print(e)

# Insert Data To Table

n = int(input("Enter the number of Records you have to insert: "))

for i in range(n):
    nm = input("Enter the Name: ")
    sub = input("Enter the Subject: ")
    insert_data = f"insert into studinfo(name, sub)values ('{nm}', '{sub}')"
print("Data Inserted!")

try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)

# Update Data To Table
