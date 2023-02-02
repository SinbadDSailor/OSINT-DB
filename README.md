# OSINT-DB

OSINT-DB is a project created with the aim of centralizing data during investigations. At the current stage, it consists of a database containing only the necessary attributes and a terminal menu.
## Future Goals

It is planned to be added in future versions:
- Relationships between persons from the database with a graphic display
- Automatic collection of outputs from existing OSINT projects
- Database expansion
- Migration of individual records and the complete database
- Code optimization
***
## Features

- Entering records one by one
- Input of multiple records using CSV and JSON files
- Delete records
- Edit existing records
- Output the complete database to the terminal, CSV or JSON file
- Creation of individual report in pdf
- Creation of complete database report in pdf
***
## Menu Tree

    [MAIN MENU]
    [1] Input options
        [1] Individual input
        [2] Input from CSV
        [3] Input form JSON
        [4] Back
    [2] Output options
        [1] Bulk output to terminal
        [2] Bulk output to CSV
        [3] Bulk output to JSON
        [4] Generate individual report
        [5] Generate complete DB report
        [6] Back
    [3] Database editor
        [1] Edit records
        [2] Delete record
        [3] Back
    [4] Advanced options
        [1] Setup database
        [2] Back
    [5] Exit
***
## Usage

After starting the main.py file, it is necessary to select the **Setup database** option in the menu in order to create the database.

This process needs to be done only at the initial launch of OSINT-DB.

After initial setup, OSINT-DB is ready for data entry.

Data entry can be done manually one by one or through CSV and JSON files.

All output files will be created in the output folder.

***

## Report example

![Report](/media/report_example.png)


***

## License
MIT © OSINT-DB

Creator - 
