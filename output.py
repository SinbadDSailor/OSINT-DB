import logging
import os
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

def output_print_term(): # Print output to terminal function---------->
    file_path = "storage/osint.db"

    conn = create_connection(file_path)

    print_out_comm = """SELECT * FROM persons;"""

    if conn is not None:
        table = pd.read_sql_query(print_out_comm, conn)
        print(table)
        conn.close()
    else:
        logger.error("Error while trying to output to terminal")
                         # Print output to terminal function---------/>

def output_csv(): # Export to CSV function---------->
    csv_file = input("Enter CSV file name: ")
    csv_file_full = csv_file + ".csv"
    file_path = "storage/osint.db"
    out_parent_path = "output"
    out_csv = os.path.join(out_parent_path, csv_file_full)

    conn = create_connection(file_path)

    print_out_comm = """SELECT * FROM persons;"""

    if conn is not None:
        table = pd.read_sql_query(print_out_comm, conn)
        table.to_csv(out_csv, index=False)
        print(f"Successfully exported to {out_csv}")
        conn.close()
    else:
        logger.error("Error while trying to output to CSV")
                  # Export to CSV function---------/>

def output_json(): # Export to JSON function---------->
    json_file = input("Enter JSON file name: ")
    json_file_full = json_file + ".json"
    file_path = "storage/osint.db"
    out_parent_path = "output"
    out_json = os.path.join(out_parent_path, json_file_full)

    print_out_comm = """SELECT * FROM persons;"""

    conn = create_connection(file_path)
    cursor = conn.execute(print_out_comm)

    if conn is not None:
        json_obj = pd.read_sql_query(print_out_comm, conn)
        json_obj.squeeze().to_json(out_json, orient="records", indent=4)
        print(f"Successfully exported to {out_json}")
        conn.close()
    else:
        logger.error("Error while trying to output JSON")
        # Export to JSON function---------/>
