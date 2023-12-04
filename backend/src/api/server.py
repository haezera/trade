from flask import Flask, request, jsonify
import mysql.connector
import src.api.SQLFunctions as sqlf
import src.api.auth as auth
import src.stock as stock
import src.helpers as helpers
import src.backtester as bt
# SQL db connection
db = mysql.connector.connect(
    host="localhost",
    user="test",
    password='tester',
)

# SQL cursor and setup
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
    password VARCHAR(255))
""")
cursor.execute("""
CREATE TABLE sessions (
    session_id VARCHAR(255),
    user_id VARCHAR(255)
)
""")
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return {"message": "You accessed the root!"}


@app.route("/clear", methods=["DELETE"])
def clear():
    print("Clearing database...")
    cursor.execute("DROP DATABASE IF EXISTS pytrading")
    db.commit()
    cursor.execute("CREATE DATABASE IF NOT EXISTS pytrading")
    cursor.execute("USE pytrading")
    cursor.execute("""
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        firstName VARCHAR(255),
        lastName VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255))
    """)
    cursor.execute("""
    CREATE TABLE sessions (
        session_id VARCHAR(255),
        user_id VARCHAR(255)
    )
    """)
    db.commit()


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
    print(response)
    if "error" in response:
        return response, 400
    return {"response": response}


@app.route("/user/<sessionId>/pw/update", methods=["PUT"])
def pw_update(sessionId):
    body = request.json
    cursor.execute(sqlf.fetch_user_id, (sessionId,))
    user_id = cursor.fetchone()
    if user_id is None:
        return {"error": "sessionId is invalid"}, 400
    user_id = user_id[0]
    response = auth.pwUpdate(
        user_id,
        body["oldPassword"],
        body["newPassword"],
        db,
        cursor
    )
    print(response)
    if "error" in response:
        return response, 400
    return {"response": response}


@app.route("/user/<sessionId>/email/update", methods=["PUT"])
def email_update(sessionId):
    body = request.json
    cursor.execute(sqlf.fetch_user_id, (sessionId,))
    user_id = cursor.fetchone()
    if user_id is None:
        return {"error": "sessionId is invalid"}, 400
    user_id = user_id[0]
    response = auth.emailUpdate(
        user_id,
        body["newEmail"],
        body["password"],
        db,
        cursor
    )
    print(response)
    if "error" in response:
        return response, 400
    return {"response": response}


@app.route("/stock/<sessionId>/<ticker>/incomestmt", methods=["GET"])
def getIncomeStmt(sessionId, ticker):
    try:
        cursor.execute(sqlf.fetch_user_id, (sessionId,))
        user_id = cursor.fetchone()
        if user_id is None:
            return {"error": "sessionId is invalid"}, 400
        user_id = user_id[0]
        # Set up stock class
        stockObj = stock.Stock(ticker)
        # Get income statement
        response = stockObj.incomeStmt()
        if response.empty:
            return {"error": "No data found for ticker"}, 400
        return {"results": response.to_json()}
    except Exception:
        return {"error": "Invalid stock"}, 400


@app.route("/stock/<sessionId>/<ticker>/balancesheet", methods=["GET"])
def getBalanceSheet(sessionId, ticker):
    try:
        cursor.execute(sqlf.fetch_user_id, (sessionId,))
        user_id = cursor.fetchone()
        if user_id is None:
            return {"error": "sessionId is invalid"}, 400
        user_id = user_id[0]
        # Set up stock class
        stockObj = stock.Stock(ticker)
        # Get income statement
        response = stockObj.balanceSheet()
        if response.empty:
            return {"error": "No data found for ticker"}, 400
        return {"results": response.to_json()}
    except Exception:
        return {"error": "Invalid stock"}, 400


@app.route("/stock/<sessionId>/<ticker>/cashflow", methods=["GET"])
def getCashFlow(sessionId, ticker):
    try:
        cursor.execute(sqlf.fetch_user_id, (sessionId,))
        user_id = cursor.fetchone()
        if user_id is None:
            return {"error": "sessionId is invalid"}, 400
        user_id = user_id[0]
        # Set up stock class
        stockObj = stock.Stock(ticker)
        # Get income statement
        response = stockObj.cashFlow()
        if response.empty:
            return {"error": "No data found for ticker"}, 400
        return {"results": response.to_json()}
    except Exception:
        return {"error": "Invalid stock"}, 400


@app.route("/stock/<sessionId>/<ticker>/historical", methods=["GET"])
def getHistorical(sessionId, ticker):
    try:
        startDate = request.args.get("startDate")
        if startDate is None:
            return {"error": "startDate is required"}, 400
        endDate = request.args.get("endDate")
        if endDate is None:
            return {"error": "endDate is required"}, 400

        cursor.execute(sqlf.fetch_user_id, (sessionId,))
        user_id = cursor.fetchone()
        if user_id is None:
            return {"error": "sessionId is invalid"}, 400
        user_id = user_id[0]

        # Set up stock class
        stockObj = stock.Stock(ticker)
        # Get income statement
        response = stockObj.history(startDate, endDate)
        if response.empty:
            return {"error": "No data found for ticker"}, 400

        return {"results": response.to_json()}
    except Exception:
        return {"error": "Invalid stock"}, 400


@app.route("/stock/<sessionId>/<ticker>/sma", methods=["GET"])
def getSma(sessionId, ticker):
    try:
        startDate = request.args.get("startDate")
        if startDate is None:
            return {"error": "startDate is required"}, 400
        endDate = request.args.get("endDate")
        if endDate is None:
            return {"error": "endDate is required"}, 400

        cursor.execute(sqlf.fetch_user_id, (sessionId,))
        user_id = cursor.fetchone()
        if user_id is None:
            return {"error": "sessionId is invalid"}, 400
        user_id = user_id[0]

        # Set up stock class
        stockObj = stock.Stock(ticker)
        # Get income statement
        response = helpers.smaPeriod(stockObj.data, startDate, endDate)
        if response is None:
            return {"error": "No data found for ticker"}, 400
        return {"results": response}
    except Exception:
        return {"error": "Invalid stock"}, 400


@app.route("/stock/<sessionId>/<ticker>/awsm", methods=["GET"])
def getAwsm(sessionId, ticker):
    try:
        startDate = request.args.get("startDate")
        if startDate is None:
            return {"error": "startDate is required"}, 400
        endDate = request.args.get("endDate")
        if endDate is None:
            return {"error": "endDate is required"}, 400

        cursor.execute(sqlf.fetch_user_id, (sessionId,))
        user_id = cursor.fetchone()
        if user_id is None:
            return {"error": "sessionId is invalid"}, 400
        user_id = user_id[0]

        # Set up stock class
        stockObj = stock.Stock(ticker)
        # Get income statement
        response = helpers.aoPeriod(stockObj.data, startDate, endDate)
        if response is None:
            return {"error": "No data found for ticker"}, 400
        return {"results": response}
    except Exception:
        return {"error": "Invalid stock"}, 400


@app.route("/stock/<sessionId>/<ticker>/vwap", methods=["GET"])
def getVwap(sessionId, ticker):
    try:
        startDate = request.args.get("startDate")
        if startDate is None:
            return {"error": "startDate is required"}, 400
        endDate = request.args.get("endDate")
        if endDate is None:
            return {"error": "endDate is required"}, 400

        cursor.execute(sqlf.fetch_user_id, (sessionId,))
        user_id = cursor.fetchone()
        if user_id is None:
            return {"error": "sessionId is invalid"}, 400
        user_id = user_id[0]

        # Set up stock class
        stockObj = stock.Stock(ticker)
        # Get income statement
        response = helpers.vwapPeriod(stockObj.data, startDate, endDate)
        if response is None:
            return {"error": "No data found for ticker"}, 400
        return {"results": response}
    except Exception:
        return {"error": "Invalid stock"}, 400

"""
@app.route("/stock/backtester/<sessionId>/<ticker>/sma", methods=["GET"])
def backtestAwsm(sessionId, ticker):
    try:
        startDate = request.args.get("startDate")
        if startDate is None:
            return {"error": "startDate is required"}, 400
        endDate = request.args.get("endDate")
        if endDate is None:
            return {"error": "endDate is required"}, 400

        cursor.execute(sqlf.fetch_user_id, (sessionId,))
        user_id = cursor.fetchone()
        if user_id is None:
            return {"error": "sessionId is invalid"}, 400
        user_id = user_id[0]

        # Set up stock class
        stockObj = stock.Stock(ticker)
        # Get income statement
        response = helpers.smaPeriod(stockObj.data, startDate, endDate)
        print(response)
        response = bt.backTester(stock.data, response)
        if response is None:
            return {"error": "No data found for ticker"}, 400
        return {"results": response}
    except Exception:
        return {"error": "Invalid stock"}, 400
"""
