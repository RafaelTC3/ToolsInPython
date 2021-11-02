from .message import csv_to_json
from .config import Path
from .import_mongo import insert_data, update_data


def init_process():
    print(
        "Select: \n 1 - To scan and insert data extracted from excel file in Mongo\n"
        " 2 - To update Mongo documents"
    )
    option = input()
    if option == '1':
        try:
            print("Converting Excel data to JSON")
            csv_to_json(
                Path["excelFilePath"],
                Path["csvFilePath"],
                Path["jsonFilePath"],
                Path["newCsvFile"],
            )
        except Exception as ex:
            print(f"Failed to convert Excel data to JSON Exception: {ex}")

        try:
            print("Inserting Data In Database")
            insert_data(Path["jsonFilePath"])
        except Exception as ex:
            print("Error Inserting data in database", ex)
    else:
        try:
            update_data()
        except Exception as ex:
            print("Error updating data in database", ex)
