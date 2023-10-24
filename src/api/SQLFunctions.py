insert_user = """INSERT INTO Users (
    sessionId,
    firstName,
    lastName,
    email,
    password,
    loggedin
) VALUES (%s, %s, %s, %s, %s, %s)"""

find_user = """
SELECT
    CASE
        WHEN EXISTS (
            SELECT 1
            FROM users
            WHERE id = %d
        )
        THEN 1
        ELSE 0
    END AS element_exists;
"""

check_password = """
SELECT password FROM users WHERE id = %s AND password = %s
"""
