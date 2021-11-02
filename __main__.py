import excel_data_extractor.select_extraction_action
from base64TokenGenerator import select_action
import readfile


# Open the config.py file and set the variables
def select_script():
    print(f'Select the script you want to run\n 1- Encoding functions\n 2- Reading Files\n 3- Extraction functions')
    option = input()
    if option == '1':
        select_action()
    elif option == '2':
        readfile.replace_csv_value()
    elif option == '3':
        excel_data_extractor.select_extraction_action.init_process()
    else:
        print("Invalid option")


if __name__ == '__main__':
    select_script()
