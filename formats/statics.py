from enum import Enum
import os
import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)


class FileFormats(Enum):
    CSV = "csv"
    XLSX = "xlsx"
    JSON = "json"


# creating files folder
def create_files_folder():
    if not os.path.exists("files"):
        logging.info("[x] Creating [ files ] folder")
        os.makedirs("files")
