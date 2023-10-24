import mysql.connector

password = input("What is your password?: ")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS pytrading")
cursor.execute("USE pytrading")
cursor.execute("""
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sessionId VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    loggedin TINYINT)
""")


db.commit()
