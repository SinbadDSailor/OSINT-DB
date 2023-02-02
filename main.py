#!/usr/bin/env python3
import time
import logging
from input import input_main
from bulk_import import bulk_csv_import, bulk_json_import
from output import output_print_term, output_csv, output_json
from db_man import create_connection, terminate_conn
from db_setup import db_main
from database_editor import db_editor_main, delete_record
from pdf_report import pdf_report_main
from bulk_pdf_report import bulk_pdf_report

#Logging setup ------------------>
filenm = "storage/log.log"
fmat = "%(levelname)s: %(asctime)s | %(name)s | %(funcName)s | %(message)s"
logging.basicConfig(filename=filenm, level=logging.DEBUG, format=fmat, filemode="w")
logger = logging.getLogger(__name__)
#Logging setup -----------------/>

file_path = "storage/osint.db"

def main_options():
    print("    MAIN MENU")
    print("[1] Input options")
    print("[2] Output options")
    print("[3] Database editor")
    print("[4] Advanced options")
    print("[5] Exit")
    print("")

def advanced_options():
    print("[1] Setup database")
    print("[2] Back")

def input_options():
    print("[1] Individual input")
    print("[2] Input from CSV")
    print("[3] Input from JSON")
    print("[4] Back")

def output_options():
    print("[1] Bulk output to terminal")
    print("[2] Bulk output to CSV")
    print("[3] Bulk output to JSON")
    print("[4] Generate individual report")
    print("[5] Generate complete DB report")
    print("[6] Back")

def database_editor():
    print("[1] Edit records")
    print("[2] Delete record")
    print("[3] Back")

def banner():
    print("""
 ██████╗ ███████╗██╗███╗   ██╗████████╗   ██████╗ ██████╗ 
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝   ██╔══██╗██╔══██╗
██║   ██║███████╗██║██╔██╗ ██║   ██║█████╗██║  ██║██████╔╝
██║   ██║╚════██║██║██║╚██╗██║   ██║╚════╝██║  ██║██╔══██╗
╚██████╔╝███████║██║██║ ╚████║   ██║      ██████╔╝██████╔╝
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝      ╚═════╝ ╚═════╝                                                                                                                            
""")

def main():
    banner()
    create_connection(file_path)
    while True:     #Main menu loop ----->
        main_options()
        main_option = int(input("Enter your option: "))
        if main_option == 1:
            while True:     #Input options menu loop ----->
                input_options()
                sub_in_option = int(input("Enter your option: "))
                if sub_in_option == 1:
                    input_main()
                    print("Success!")
                elif sub_in_option == 2:
                    bulk_csv_import()
                elif sub_in_option == 3:
                    bulk_json_import()
                elif sub_in_option == 4:
                    break
                else:
                    print("Invalid option") #Input options menu loop ----/>
        elif main_option == 2:
            while True:     #Output options menu loop ----->
                output_options()
                sub_out_option = int(input("Enter your option: "))
                if sub_out_option == 1:
                    output_print_term()
                elif sub_out_option == 2:
                    output_csv()
                elif sub_out_option == 3:
                    output_json()
                elif sub_out_option == 4:
                    pdf_report_main()
                elif sub_out_option == 5:
                    bulk_pdf_report()
                elif sub_out_option == 6:
                    break
                else:
                    print("Invalid option") #Output options menu loop ----/>
        elif main_option == 3:
            while True:     #Database editor menu loop ----->
                database_editor()
                sub_db_editor = int(input("Enter your option: "))
                if sub_db_editor == 1:
                    db_editor_main()
                elif sub_db_editor == 2:
                    delete_record()
                elif sub_db_editor == 3:
                    break
                else:
                    print("Invalid option")   #Database editor menu loop ----/>
        elif main_option == 4:
            while True:     #Advanced options menu loop ----->
                advanced_options()
                sub_adv_option = int(input("Enter your option: "))
                if sub_adv_option == 1:
                    db_main()
                elif sub_adv_option == 2:
                    break   
                else:
                    print("Invalid option") #Advanced options menu loop ----/>
        elif main_option == 5:
            terminate_conn()
            print("[~] Exiting..")
            time.sleep(1)
            break
        else:
            print("Invalid option")     #Main menu loop ----/>

if __name__ == "__main__":
    main()