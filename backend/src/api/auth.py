import src.api.SQLFunctions as sqlf
import src.api.password as pw
import mysql.connector
import uuid


def userRegister(
    firstName: str,
    lastName: str,
    email: str,
    password: str,
    db,
    cursor
):
    if firstName == "":
        return {"error": "First name is empty!"}
    elif lastName == "":
        return {"error": "Last name is empty!"}
    elif email == "":
        return {"error": "Email is empty!"}
    elif password == "":
        return {"error": "Password is empty!"}
    hashedPassword = pw.hashPassword(password)
    try:
        cursor.execute(sqlf.insert_user, (
            firstName, lastName, email, hashedPassword))
        cursor.fetchone()
        return "User has been registered!"
    except mysql.connector.Error as err:
        cursor.fetchone()
        print("Error: {}".format(err))
    except Exception:
        cursor.fetchone()
        return {"error": "An error within SQL has occured."}


def userLogin(
    email: str,
    password: str,
    db,
    cursor
):
    # Fetch hashed password
    try:
        cursor.execute(sqlf.fetch_email, (email,))
    except Exception:
        return {"error": "Email is invalid"}
    user_id = cursor.fetchone()
    if (user_id is None):
        return {"error": "Email is invalid"}
    user_id = user_id[0]
    try:
        cursor.execute(sqlf.check_password, (user_id,))
    except Exception:
        return {"error": "Password is invalid"}
    hashed_pw = cursor.fetchone()
    if hashed_pw is None:
        return {"error": "Password is invalid"}
    hashed_pw = hashed_pw[0]
    try:
        if pw.verifyPassword(hashed_pw, password) is True:
            session_id = str(uuid.uuid4())
            cursor.execute(sqlf.insert_session, (session_id, user_id))
            db.commit()
            return session_id
    except Exception:
        cursor.fetchone()
        return {"error": "Password is invalid"}


def userLogout(
    sessionId: str,
    db,
    cursor
):
    try:
        cursor.execute(sqlf.delete_a_session, (sessionId, ))
        cursor.fetchone()
        db.commit()
        return "Session has been deleted."
    except mysql.connector.Error as err:
        return {"error": "SQL Error {}".format(err)}
    except Exception:
        return {"error": "An error within SQL has occured."}


def pwUpdate(
    user_id: int,
    oldPw: str,
    newPw: str,
    db,
    cursor
):
    cursor.execute(sqlf.check_password, (user_id, ))
    hashed_pw = cursor.fetchone()
    if hashed_pw is None:
        return {"error": "Query has failed"}
    hashed_pw = hashed_pw[0]
    try:
        if pw.verifyPassword(hashed_pw, oldPw) is True:
            hashed_new_pw = pw.hashPassword(newPw)
            cursor.execute(sqlf.update_password, (hashed_new_pw, user_id))
            db.commit()
            return {"response": "Password has sucessfully been updated!"}
    except mysql.connector.Error as err:
        cursor.fetchone()
        return {"error: Something went wrong -> {}".format(err)}
    except Exception:
        cursor.fetchone()
        return {"error": "Password is incorrect!"}


def emailUpdate(
    user_id: int,
    newEmail: str,
    password: str,
    db,
    cursor
):
    cursor.execute(sqlf.check_password, (user_id, ))
    hashed_pw = cursor.fetchone()
    if hashed_pw is None:
        return {"error": "Password query has failed"}
    hashed_pw = hashed_pw[0]
    try:
        if pw.verifyPassword(hashed_pw, password) is True:
            cursor.execute(sqlf.update_email, (newEmail, user_id))
            db.commit()
            return {"response": "Email has successfully been changed."}
        else:
            return {"error": "Password is incorrect!"}
    except mysql.connector.Error as err:
        cursor.fetchone()
        return {"error": "Something went wrong -> {}".format(err)}
    except Exception:
        return {"error": "An error has occured!"}

