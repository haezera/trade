from flask import Flask
from flask import request 
from flask import jsonify 
import mysql.connector 

# You are required to run the setup first. 

password = input("What is your mySQL root password?: ")

# SQL db connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="pytrading"
)

# SQL cursor
cursor = db.cursor()

app = Flask(__name__)


@app.route("/")
def root():
    return {"message": "You accessed the root!"}
