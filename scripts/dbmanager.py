" This file contains the functions to manage the database of users."

# IMPORT MODULES

import argparse
import sqlite3
from sqlite3 import Error
import sys
import hashlib
import random 


# PARAMETERS

path = r"/home/seed/luhn_db"  # Important: use absolute path to db.


# FUNCTIONS

def arg_parsing():

    "Function to parse arguments of main.py"

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=str, help="username to be added to db")
    parser.add_argument("-p", type=str, help="password to be added to db")
    parser.add_argument("-u", type=str,
                        help="username to access the cn validation")
    args = parser.parse_args()
    username_to_be_added = args.a
    username_for_login = args.u
    password = args.p
    return username_for_login, username_to_be_added, password


def create_connection(db_file):

    "Create a database connection to a SQLite database."

    conn = None
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()

    return conn, curs


def user_db_connection(path):

    "Connect to user db and do operations."

    db_file = path + "/user.db"
    conn, curs = create_connection(db_file)
    try:
        curs.execute('SELECT count(username) FROM user')
    except Error:
        curs.execute('CREATE TABLE user (username CHAR(256), salt CHAR(256));')
        conn.commit()
        print('User table created.')

    return conn, curs


def password_db_connection(path):

    "Connect to password db and do operations."

    db_file = path + "/password.db"
    conn, curs = create_connection(db_file)
    try:
        curs.execute('SELECT count(username) FROM password')
    except Error:
        curs.execute('CREATE TABLE password (username CHAR(256),password CHAR(256));')
        conn.commit()
        print('Password table created.')

    return conn, curs


def hash_password(password, salt):

    "Hash the password."

    digest = str(salt) + password
    for i in range(1000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()

    return digest


# BODY


exit_code = ''

username_for_login, username_to_be_added, password = arg_parsing()

if (username_for_login == None and username_to_be_added == None) or (password == None):
    print('Missing arguments.')
else:
    user_conn, user_curs = user_db_connection(path)
    pwd_conn, pwd_curs = password_db_connection(path)
    if username_for_login != None:
        user_curs.execute('SELECT salt FROM user WHERE (username="{}");'.format(username_for_login))
        salt = user_curs.fetchall()[0][0]
        if len(salt) > 0:
            salt = float(salt)
            hashed_pwd = hash_password(password, salt)
            pwd_curs.execute('SELECT count(*) FROM password WHERE (username="{}" AND password="{}");'.format(username_for_login, hashed_pwd))
            if int(pwd_curs.fetchall()[0][0]) > 0:
                exit_code = 0
    else:
        user_curs.execute('SELECT count(*) FROM user WHERE (username="{}");'.format(username_to_be_added))
        user_exists = user_curs.fetchall()[0][0]
        if user_exists == 0:
            salt = str(random.random())
            user_curs.execute('INSERT INTO user (username, salt) VALUES("{}", "{}");'.format(username_to_be_added, salt))
            user_conn.commit()
            hashed_pwd = hash_password(password, salt)
            pwd_curs.execute('INSERT INTO password (username, password) VALUES("{}", "{}");'.format(username_to_be_added, hashed_pwd))
            pwd_conn.commit()
            exit_code = 0
        else:
            print('User already exists.')
            exit_code = 1

user_conn.close()
pwd_conn.close()
sys.exit(exit_code)
