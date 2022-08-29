import os
import logging


def get_file_path(file_name: str):
    curr_work_dir = os.getcwd()
    return os.path.join(curr_work_dir, "files", file_name)


# creating files folder
def create_files_folder():
    if not os.path.exists("files"):
        logging.info("[+] Creating [ files ] folder")
        os.makedirs("files")
