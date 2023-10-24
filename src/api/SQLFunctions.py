import mysql.connector

password = input("What is your password?: ")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pytrading")
mycursor.execute("USE pytrading")
mycursor.execute("""CREATE TABLE Users(
    UserID VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    loggedin int
)""")
print("pytrading database initialised!")
print("mySQL server initialised!")
