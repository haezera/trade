import SQLFunctions as sqlf
import password as pw


def userRegister(
    firstName: str,
    lastName: str,
    email: str,
    password: str,
    db,
    cursor
):
    if firstName == "":
        raise Exception("First name is empty!")
    elif lastName == "":
        raise Exception("Last name is empty!")
    elif email == "":
        raise Exception("Email is empty!")
    elif password == "":
        raise Exception("Password is empty!")
    hashedPassword = pw.hashPassword(password)
    cursor.execute(sqlf.insert_user, (
        "empty", firstName, lastName, email, hashedPassword, 0))
    db.commit()
    return "User has been registered!"
