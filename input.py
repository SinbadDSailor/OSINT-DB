import logging
import sqlite3
from sqlite3 import Error

#Logging setup ------------------>
filenm = "storage/log.log"
fmat = "%(levelname)s: %(asctime)s | %(name)s | %(funcName)s | %(message)s"
logging.basicConfig(filename=filenm, level=logging.DEBUG, format=fmat, filemode="w")
logger = logging.getLogger(__name__)
#Logging setup -----------------/>

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        logger.error(e)

    return conn

def exec_comm(conn, create_table_sql, in_vars):
    try:
        c = conn.cursor()
        c.execute(create_table_sql, in_vars)
    except Error as e:
        logger.error(e)

def input_main():
    file_path = "storage/osint.db"

    print("Enter data value by value")
    print("If you don't want to input data, just skip input question")
    print("---------------------------------------------------------")
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    nname = input("Enter nick name: ")
    ucid = input("Enter UCID: ")
    b_date = input("Enter birth date: ")
    address = input("Enter address: ")
    e_address = input("Enter email address: ")
    phone = input("Enter phone number: ")
    facebook = input("Enter facebook account: ")
    instagram = input("Enter instagram account: ")
    twitter = input("Enter twitter account: ")
    linkedin = input("Enter linkedin account: ")
    github = input("Enter github account: ")
    photo = input("Enter path to the photo: ")

    input_vars_checker = (f_name, l_name, nname, ucid, b_date, address, e_address, phone, facebook, instagram, twitter, linkedin, github, photo)
    input_vars = ()
    for val in input_vars_checker:
        if val == "":
            val = None
            input_vars = input_vars + (val,)
        else:
            input_vars = input_vars + (val,)

    ind_input_comm = """INSERT INTO persons 
    (id, 
    first_name, 
    last_name,
    nick_name,
    ucid, 
    birth_date, 
    address, 
    email_address, 
    phone_number, 
    facebook, 
    instagram, 
    twitter, 
    linkedin, 
    github,
    photo) VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    conn = create_connection(file_path)

    if conn is not None:
        exec_comm(conn, ind_input_comm, input_vars)
        conn.commit()
        conn.close()
    else:
        logger.error("Error while trying to individual input")