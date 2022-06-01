import pytest
import os.path
from .ConfigTest import Path, Sheet
from excel_data_extractor import message


def test_read_excel_write_csv_create_json():
    print(os.getcwd())
    message.input = lambda: "no"
    message.csv_to_json(Sheet["sheetName"],
                        Path["excelFilePath"],
                        Path["csvFilePath"],
                        Path["jsonFilePath"],
                        Path["newCsvFile"])
    assert os.path.exists(Path["csvFilePath"]) == True
    assert os.path.exists(Path["jsonFilePath"]) == True
    assert os.path.exists(Path["newCsvFile"]) == True
