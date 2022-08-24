import os
from typing import List
import json
import logging
import csv

from openpyxl import Workbook

from formats.statics import create_files_folder

DataType = List[List[str]]

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)


def get_file_path(file_name: str):
    curr_work_dir = os.getcwd()
    return os.path.join(curr_work_dir, "files", file_name)


class Json:
    def __init__(
        self, filename: str, data: DataType = None, keys: List[str] = None
    ) -> None:
        self._filename = filename
        self._keys = keys
        self._data = data

    def __call__(self):
        if not self._data:
            return

        filename = f"{self._filename}.json"
        mapped_values = []
        if not self._keys:
            logging.error(f"[x] Please provide valid keys")
            return

        try:
            for rows in self._data:
                dictionary = dict(zip(self._keys, rows))
                mapped_values.append(dictionary)
            json_data = json.dumps(mapped_values, indent=4)
            create_files_folder()
            filepath = get_file_path(filename)

            with open(filepath, "w", encoding="utf-8") as json_file:
                json_file.write(json_data)

            logging.info(f"[+] Successfully saved {filename}")
        except IOError:
            logging.error(
                f"[-] Error while saving [ {filename} ], Please check the values of your data"
            )


class Excel:
    def __init__(
        self,
        filename: str,
        data: DataType = None,
        headers: List[str] = None,
        sheet_name: str = None,
    ) -> None:
        self._filename = filename
        self._data = data
        self._headers = headers
        self._sheet_name = sheet_name

    def __call__(self):
        wb = Workbook()
        page = wb.active
        filename = f"{self._filename}.xlsx"

        if self._headers:
            page.append(self._headers)
        if self._sheet_name:
            page.title = self._sheet_name

        try:
            create_files_folder()
            for value in self._data:
                page.append(value)
            filepath = get_file_path(filename)
            wb.save(filepath)
            logging.info(f"[+] Successfully saved {filename}")
        except TypeError:
            logging.error(
                f"[-] Error while saving [ {filename} ], "
                "Please check the values of your data"
            )
        except PermissionError:
            logging.warning(
                f"[x] Error while saving [ {filename} ], "
                "Please close the file before adding new data"
            )


class Csv:
    def __init__(
        self, filename: str, data: DataType = None, headers: List[str] = None
    ) -> None:
        self._filename = filename
        self._data = data
        self._headers = headers

    def __call__(self):
        filename = f"{self._filename}.csv"
        create_files_folder()
        filepath = get_file_path(filename)

        csv_file = open(filepath, "w", newline="")
        csv_writer = csv.writer(csv_file)

        if self._headers is not None:
            csv_writer.writerow(self._headers)
        try:
            for values in self._data:
                csv_writer.writerow(values)
            csv_file.close()
            logging.info(f"[+] Successfully saved {filename}")
        except TypeError:
            logging.error(
                f"[-] Error while saving [ {filename} ], Please check the values of your data"
            )
