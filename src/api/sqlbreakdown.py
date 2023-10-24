import mysql.connector

password = input("What is your password?: ")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password
)

cursor = db.cursor()
cursor.execute("DROP DATABASE pytrading")


db.commit()
