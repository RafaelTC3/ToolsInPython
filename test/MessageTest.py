import unittest
import os.path
from ConfigTest import Path, Sheet
from excel_data_extractor import message


class MessageTest(unittest.TestCase):
    def test_read_excel_write_csv_create_json(self):
        message.input = lambda: "no"
        message.csv_to_json(Sheet["sheetName"],
                            Path["excelFilePath"],
                            Path["csvFilePath"],
                            Path["jsonFilePath"],
                            Path["newCsvFile"])
        self.assertEqual(os.path.exists(Path["csvFilePath"]), True)
        self.assertEqual(os.path.exists(Path["jsonFilePath"]), True)
        self.assertEqual(os.path.exists(Path["newCsvFile"]), True)


if __name__ == '__main__':
    unittest.main()
