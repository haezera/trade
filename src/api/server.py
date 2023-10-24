from flask import Flask
from flask import request
from flask import jsonify
import mysql.connector
import SQLFunctions as sqlf
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
cursor.execute("DROP DATABASE IF EXISTS pytrading")
cursor.execute("CREATE DATABASE IF NOT EXISTS pytrading")
cursor.execute("USE pytrading")
cursor.execute("""
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    loggedin TINYINT(1))
""")
cursor.execute("""
CREATE TABLE sessions (
    session_id VARCHAR(255),
    user_id VARCHAR(255)
)
""")
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
    if "error" in response:
        return response, 400
    return {"response": response}


@app.route("/user/login", methods=["PUT"])
def user_login():
    body = request.json
    response = auth.userLogin(
        body["email"],
        body["password"],
        db,
        cursor
    )
    if "error" in response:
        return response, 400
    return {"session_id": response}


@app.route("/user/logout", methods=["PUT"])
def user_logout():
    body = request.json
    response = auth.userLogout(
        body["sessionId"],
        db,
        cursor
    )
    if "error" in response:
        return response, 400
    return {"response": response}


@app.route("/user/<sessionId>/pw/update", methods=["PUT"])
def pw_update(sessionId):
    body = request.json
    user_id = cursor.execute(sqlf.fetch_user_id, (sessionId,))[0]
    response = auth.pwUpdate(
        user_id,
        body["oldPassword"],
        body["newPassword"],
        db,
        cursor
    )
    if "error" in response:
        return response, 400
    return {"response": response}
