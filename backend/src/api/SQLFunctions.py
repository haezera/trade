insert_user = """INSERT INTO users (
    firstName,
    lastName,
    email,
    password
) VALUES (%s, %s, %s, %s)"""

insert_session = """
INSERT INTO sessions (
    session_id,
    user_id
) VALUES (%s, %s)
"""

find_user = """
SELECT
    CASE
        WHEN EXISTS (
            SELECT 1
            FROM users
            WHERE id = %s
        )
        THEN 1
        ELSE 0
    END AS element_exists;
"""

fetch_email = """
SELECT id FROM users WHERE email=%s
"""

fetch_user_id = """
SELECT user_id FROM sessions WHERE session_id=%s
"""

check_password = """
SELECT password FROM users WHERE id=%s
"""

update_password = """
UPDATE users
SET password=%s
WHERE id=%s
"""

update_email = """
UPDATE users
SET email=%s
WHERE id=%s
"""

print_table = """
SELECT * FROM users
"""

delete_a_session = """
DELETE FROM sessions WHERE session_id=%s
"""
