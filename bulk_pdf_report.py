from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date
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

def bulk_pdf_report():
    file_path = "storage/osint.db"
    conn = create_connection(file_path)
    cursor = conn.cursor()

    iwidth, iheight = 150, 150
    today = date.today().strftime("%d-%m-%Y")
    
    file_name = "output/db_report.pdf"
    print_out_comm = "SELECT * FROM persons;"
    paper = canvas.Canvas(file_name, pagesize=A4)

    cursor.execute(print_out_comm)
    data_grabber = cursor.fetchall()
    c = 0
    #Main loop------------------------------------->
    for i in data_grabber:
        c += 1
        get_col = i
        paper.setLineWidth(.5)
        pdfmetrics.registerFont(TTFont('Consolas', 'fonts/consola.ttf'))
        paper.setFont('Consolas', 14)

        paper.line(50, 785, 275, 785)
        paper.line(500, 785, 550, 785)
        if get_col[14] is None:
            paper.drawImage("media/no_img.jpg", 50, 625, width=iwidth, height=iheight, preserveAspectRatio=True)
        elif get_col[14] == "":
            paper.drawImage("media/no_img.jpg", 50, 625, width=iwidth, height=iheight, preserveAspectRatio=True)
        else:
            paper.drawImage(get_col[14], 50, 625, width=iwidth, height=iheight, preserveAspectRatio=True)
        paper.drawString(105, 601, "ID:")
        paper.drawRightString(150, 601, str(get_col[0]))
        paper.rect(102, 595, 53, 20, stroke=1, fill=0)
        paper.drawImage("media/logo.png", 270, 685, width=250, height=200, preserveAspectRatio=True)
        paper.line(50, 585, 550, 585)
        paper.drawString(300, 590, f"Report generated on: {today}")
        paper.drawString(55, 35, f"Page | {c}")

        #Data table--------------------------------------------------->
        x_line_list = [560, 535, 510, 485, 460, 435, 410, 385, 360, 335, 310, 285, 260, 235]
        y_line_list = [50, 200, 550]

        for i in x_line_list:
            paper.line(50, i, 550, i)

        for i in y_line_list:
            paper.line(i, 235, i, 560)

        paper.drawString(55, 540, "First Name")
        paper.drawString(55, 515, "Last Name")
        paper.drawString(55, 490, "Nick Name")
        paper.drawString(55, 465, "UCID")
        paper.drawString(55, 440, "Birth date")
        paper.drawString(55, 415, "Address")
        paper.drawString(55, 390, "Email address")
        paper.drawString(55, 365, "Phone number")
        paper.drawString(55, 340, "Facebook")
        paper.drawString(55, 315, "Instagram")
        paper.drawString(55, 290, "Twitter")
        paper.drawString(55, 265, "Linkedin")
        paper.drawString(55, 240, "GitHub")

        paper.drawRightString(540, 540, str(get_col[1]))
        paper.drawRightString(540, 515, str(get_col[2]))
        paper.drawRightString(540, 490, str(get_col[3]))
        paper.drawRightString(540, 465, str(get_col[4]))
        paper.drawRightString(540, 440, str(get_col[5]))
        paper.drawRightString(540, 415, str(get_col[6]))
        paper.drawRightString(540, 390, str(get_col[7]))
        paper.drawRightString(540, 365, str(get_col[8]))
        paper.drawRightString(540, 340, str(get_col[9]))
        paper.drawRightString(540, 315, str(get_col[10]))
        paper.drawRightString(540, 290, str(get_col[11]))
        paper.drawRightString(540, 265, str(get_col[12]))
        paper.drawRightString(540, 240, str(get_col[13]))
        #Data table--------------------------------------------------/>


        paper.line(50, 50, 550, 50)
        paper.showPage()
    paper.save()
    print(f"Successfully generated {file_name} report!")

    if conn is not None:
        conn.close()
    else:
        logger.error("Error while trying to terminate connection")
