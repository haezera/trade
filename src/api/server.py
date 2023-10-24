from flask import Flask
from flask import request 
from flask import jsonify 
import mysql.connector 

# You are required to run the setup first. 

password = input("What is your mySQL root password?: ")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="pytrading"
)

app = Flask(__name__)


@app.route("/")
def root():
    return {"message": "You accessed the root!"}
