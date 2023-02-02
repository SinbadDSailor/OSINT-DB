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

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        logger.error(e)

def db_main():
    file_path = "storage/osint.db"

    a_table = """CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    nick_name TEXT,
    ucid TEXT,
    birth_date TEXT,
    address TEXT,
    email_address TEXT,
    phone_number TEXT,
    facebook TEXT,
    instagram TEXT,
    twitter TEXT,
    linkedin TEXT,
    github TEXT,
    photo TEXT);
    """

    conn = create_connection(file_path)

    if conn is not None:
        create_table(conn, a_table)
        conn.commit()
        print("[~] Database successfully created!")
        conn.close()
    else:
        logger.error("Error while creating Database")

