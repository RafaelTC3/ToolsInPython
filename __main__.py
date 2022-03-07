from excel_data_extractor import select_extraction_action
import Base64TokenGenerator
import ReadFile


# Open the config.py file and set the variables
def select_script():
    print(f'Select the script you want to run\n 1- Encoding functions\n 2- Reading Files\n 3- Extraction functions')
    option = input()
    if option == '1':
        Base64TokenGenerator.select_action()
    elif option == '2':
        print("Insert the csv file path")
        csv_file_path = input()
        print("Insert column name to have its value updated")
        column_name = input()
        print("Insert value to be updated")
        new_column_value = input()
        ReadFile.replace_csv_value(csv_file_path, column_name, new_column_value)
    elif option == '3':
        select_extraction_action.init_process()
    else:
        print("Invalid option")


if __name__ == '__main__':
    select_script()
