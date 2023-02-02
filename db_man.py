import time
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
    global conn
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        logger.info("Connected to database")
        print("----------------------------")
        print("[~] Connecting to Database..")
        time.sleep(1)
        print("[~] Connected")
        print("[~] SQLite version: " + sqlite3.version)
        print("----------------------------")
    except Error as e:
        logger.error(e)

def terminate_conn():
    print("[~] Closing connection..")
    time.sleep(1)
    print("[~] Connection closed")
    conn.close()
    logger.info("Connection closed")

