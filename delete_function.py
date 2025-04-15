import os
import time

def get_files_in_folder(folder_path):
    files = []
    if not os.path.exists(folder_path):
        print(f"Folder does  not exist: {folder_path}")
        return files
    files = os.listdir(folder_path)
    return files

def create_delete_list(files):
    delete_files_list = []
    if not files:
        print("No files found in the folder.")
        return delete_files_list
    for file in files:
        # Check if the file is a screenshot (you can adjust the condition as needed)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            delete_files_list.append(file)
    return delete_files_list

def delete_files(delete_files_list, parent_folder_path):
    if not delete_files_list:
        print("No files to delete.")
        return
    for file in delete_files_list:
        file_path = os.path.join(parent_folder_path, file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
        time.sleep(0.25)