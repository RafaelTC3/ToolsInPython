import os
import pandas as pd


def csv_to_json(xls_file_path, csv_file_path, json_file_path, update_csv_file_path):
    """
    Methods to transform a csv file into a json file
    :param xls_file_path:
    :param csv_file_path:
    :param json_file_path:
    :param update_csv_file_path:
    :return:
    """

    def transform_xlsx_to_csv(xlsx_file, csv_path):
        """
        The input file is in .xlsx format, to make it easier to manipulate it, let's transform it into .csv format
        :param xlsx_file: Path where the file is
        :param csv_path: Path where the csv file will be save
        :return: csv file
        """
        print(" - Starting method transform_xlsx_to_csv")
        print(" - Converting .xlsx to .csv")

        read_file = pd.read_excel(xlsx_file, sheet_name="", engine="openpyxl")
        csv_file = read_file.to_csv(csv_path, index=None, header=True)

        print(" - Generating new .csv file")
        print(" - Finishing method transform_xlsx_to_csv")

        return csv_file

    def update_csv_headers(csv_path, update_csv_path):
        """
        Change the file headers passing the words to English and lower case
        :param csv_path: Path where the csv file is
        :param update_csv_path:
        :return: dataframe file
        """
        print(" - Starting method update_csv_headers")
        print(" - Converting headers to lower and English")

        df = pd.read_csv(csv_path)
        df = df.fillna(" ")
        headers: list = df.columns.values.tolist()
        print("Want to change column names? (yes/no)")
        rename = input()
        for header in headers:
            if rename == "yes":
                print(f"Insert name to replace {header}. "
                      f"Write exactly as it should be named (camelCase, snake_case, CapitalCase)")
                name = input()
                headers.insert(headers.index(header), name)

            else:
                value = header.lower()
                headers.insert(headers.index(header), value)
            headers.remove(header)

        for header in headers:
            df = df.rename(columns={df.columns[headers.index(header)]: header})

        print(" - Generating new csv")
        print(" - Finishing method update_csv_headers")

        return df.to_csv(update_csv_path, index=None, header=True)

    def create_json(update_csv_path, json_path):
        """
        Creates a JSON object in the pattern that will be saved in MongoDB
        :param update_csv_path: Path where the csv with the new headers is
        :param json_path: Path where the JSON file will be save
        :return: JSON file
        """
        print(" - Starting method create_json")
        print(" - Creating JSON file")

        df = pd.read_csv(update_csv_path)

        print(" - JSON file is created")
        print(" - Finishing method create_json")
        return df.to_json(json_path, orient='records', force_ascii=False, indent=4)

    transform_xlsx_to_csv(xls_file_path, csv_file_path)

    update_csv_headers(csv_file_path, update_csv_file_path)

    create_json(update_csv_file_path, json_file_path)

    remove_csv_file()  # Comment this line if you want to take a look into the temp csv file


def remove_csv_file():
    print(" - Removing all .csv files")

    directory = "./"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".csv")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)

    print(" - All process is done")
