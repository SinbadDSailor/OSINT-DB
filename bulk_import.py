import logging
import pandas as pd
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

def bulk_csv_import():
    path_to_csv = input("Enter path to CSV file: ")
    file_path = "storage/osint.db"
    conn = create_connection(file_path)

    try:
        ldata = pd.read_csv(path_to_csv)
        ldata.to_sql("persons", conn, if_exists="append", index=False)
        print("Successfully imported to database!")
        conn.commit()
        conn.close()
    except Error as e:
        logger.error(e)

def bulk_json_import():
    path_to_json = input("Enter path to JSON file: ")
    file_path = "storage/osint.db"
    conn = create_connection(file_path)

    try:
        ldata = pd.read_json(path_to_json)
        ldata.to_sql("persons", conn, if_exists="append", index=False)
        print("Successfully imported to database!")
        conn.commit()
        conn.close()
    except Error as e:
        logger.error(e)