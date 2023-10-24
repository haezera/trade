from flask import Flask
from flask import request
from flask import jsonify
import mysql.connector
import auth


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


@app.route("/user/register", methods=["POST"])
def userRegister():
    body = request.json
    response = auth.userRegister(
        body["firstName"],
        body["lastName"],
        body["email"],
        body["password"],
        db,
        cursor
    )
    return {"response": response}
