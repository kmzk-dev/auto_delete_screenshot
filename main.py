import delete_function as df
from config_function import get_file_path_list
import sys


if __name__ == "__main__":
    folder_path_list = get_file_path_list()
    for folder_path in folder_path_list:
        files = df.get_files_in_folder(folder_path)
        delete_files_list = df.create_delete_list(files)
        df.delete_files(delete_files_list, folder_path)
