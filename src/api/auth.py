import SQLFunctions as sqlf
import password as pw
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
    cursor.execute(sqlf.insert_user, (
        firstName, lastName, email, hashedPassword))
    db.commit()
    return "User has been registered!"


def userLogin(
    email: str,
    password: str,
    db,
    cursor
):
    # Fetch hashed password
    cursor.execute(sqlf.fetch_email, (email,))
    user_id = cursor.fetchone()[0]
    cursor.execute(sqlf.check_password, (user_id,))
    hashed_pw = cursor.fetchone()[0]
    print(hashed_pw)
    try:
        if pw.verifyPassword(hashed_pw, password) is True:
            session_id = str(uuid.uuid4())
            cursor.execute(sqlf.insert_session, (session_id, user_id))
            db.commit()
            return session_id
    except:
        return {"error": "Password is invalid"}


def userLogout(
    sessionId: str,
    db,
    cursor
):
    try:
        cursor.execute(sqlf.delete_a_session, (sessionId))
        db.commit()
        return "Session has been deleted."
    except:
        return {"error": "An error within SQL has occured."}


def pwUpdate(
    user_id: int,
    oldPw: str,
    newPw: str,
    db,
    cursor
):
    cursor.execute(sqlf.check_password, (user_id, ))
    hashed_pw = cursor.fetchone()[0]
    try:
        if pw.verifyPassword(hashed_pw, oldPw) is True:
            hashed_new_pw = pw.hashPassword(newPw)
            cursor.execute(sqlf.update_password, (hashed_new_pw, user_id))
            db.commit()
            return "Password has sucessfully been updated!"
    except:
        return {"error": "Password is incorrect!"}
