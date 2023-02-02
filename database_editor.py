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
#Records editor---------------------------------------------------->
def print_editor_options():
    print("Select the value you want to update:")
    print("[1] First Name    [2] Last Name      [3] Nick Name")
    print("[4] UCID          [5] Date of Birth  [6] Address      ")
    print("[7] Email Address [8] Phone Number   [9] Facebook         ")
    print("[10] Instagram    [11] Twitter       [12] Linkedin")
    print("[13] GitHub       [14] Photo")

def editor_options_loop(idgr):
    val_id = ""
    if idgr == 1:
        val_id = "first_name"
    elif idgr == 2:
        val_id = "last_name"
    elif idgr == 3:
        val_id = "nick_name"
    elif idgr == 4:
        val_id = "ucid"
    elif idgr == 5:
        val_id = "birth_date"
    elif idgr == 6:
        val_id = "address"
    elif idgr == 7:
        val_id = "email_address"
    elif idgr == 8:
        val_id = "phone_number"
    elif idgr == 9:
        val_id = "facebook"
    elif idgr == 10:
        val_id = "instagram"
    elif idgr == 11:
        val_id = "twitter"
    elif idgr == 12:
        val_id = "linkedin"
    elif idgr == 13:
        val_id = "github"
    elif idgr == 14:
        val_id = "photo"
    return val_id

def db_editor_main():
    file_path = "storage/osint.db"
    id_grabber = int(input("Enter ID of record you want to edit: "))
    print_editor_options()
    id_option = int(input("Enter your option: "))
    record_val = input("Enter new value: ")
    value_id = editor_options_loop(id_option)
    table_edit = f"""UPDATE persons SET {value_id} = "{record_val}" WHERE id={id_grabber};"""

    conn = create_connection(file_path)
    cursor = conn.cursor()

    if conn is not None:
        cursor.execute(table_edit)
        conn.commit()
        conn.close()
        print("Successfully updated database entry!")
    else:
        logger.error("Error!")
#Records editor--------------------------------------------------/>

#Delete record---------------------------------------------------->
def delete_record():
    file_path = "storage/osint.db"
    id_grabber = int(input("Enter ID of record you want to delete: "))
    del_comm = f"DELETE FROM persons WHERE id={id_grabber};"

    conn = create_connection(file_path)
    cursor = conn.cursor()

    if conn is not None:
        cursor.execute(del_comm)
        conn.commit()
        conn.close()
        print("Successfully deleted database record!")
    else:
        logger.error("Error while trying to terminate connection!")