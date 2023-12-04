from argon2 import PasswordHasher

ph = PasswordHasher()


def hashPassword(password):
    hashedPassword = ph.hash(password)
    return hashedPassword


def verifyPassword(hashedPassword, incomingPassword):
    return ph.verify(hashedPassword, incomingPassword)
