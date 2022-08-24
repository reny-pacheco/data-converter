from functools import wraps
import re
import logging
from typing import Optional, Tuple

from formats.formats import Json, Excel, Csv
from formats.statics import FileFormats

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)


class Convert:
    """
    Class decorator to convert data to specified file format

    :param filename: filename with extension (.xlsx, .csv, .json
    :param kwargs: arguments for each file type if needed
    """

    def __init__(self, filename: str, **kwargs) -> None:
        self._filename = filename
        self._kwargs = kwargs

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            file_name, file_ext = self.get_file_ext()
            if not self.is_valid_ext(file_ext):
                logging.error(
                    f"[+] File not saved, invalid file extension: {file_ext}"
                )
                return None

            data = func(*args, **kwargs)
            file_ext = file_ext.lower()
            if file_ext == FileFormats.JSON.value:
                Json(
                    filename=file_name,
                    data=data,
                    keys=self._kwargs.get("keys", None),
                )()
            if file_ext == FileFormats.XLSX.value:
                Excel(
                    filename=file_name,
                    data=data,
                    headers=self._kwargs.get("headers", None),
                    sheet_name=self._kwargs.get("sheet_name", None),
                )()
            if file_ext == FileFormats.CSV.value:
                Csv(
                    filename=file_name,
                    data=data,
                    headers=self._kwargs.get("headers", None),
                )()
            return data

        return wrapper

    def get_file_ext(self) -> Tuple[str, str]:
        try:
            name = re.search(".*(?=\.\w*$)", self._filename).group()
            ext = re.search("(?<=.)\w*$", self._filename).group()
            return name, ext
        except:
            logging.error(f"[-] Invalid file extension")

    def is_valid_ext(self, extension: str) -> bool:
        extensions = [ext.value for ext in FileFormats]
        return True if extension in extensions else False
