#!/usr/bin/env python3
""" encrypting_password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ password encryption """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check the password validity """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
