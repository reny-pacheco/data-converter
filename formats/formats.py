from functools import wraps
from typing import List
import json
import logging
import csv as CSV
from openpyxl import Workbook
from formats.helpers import create_files_folder, get_file_path

DataType = List[List[str]]

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)


def Csv(filename: str, headers: List[str] = None):
    """
    Convert data to excel file.

    :param filename: Name of the file
    :param headers: Column name
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)

            name = f"{filename}.csv"
            create_files_folder()
            filepath = get_file_path(name)

            csv_file = open(filepath, "w", newline="")
            csv_writer = CSV.writer(csv_file)

            if headers is not None:
                csv_writer.writerow(headers)
            try:
                for values in data:
                    csv_writer.writerow(values)
                csv_file.close()
                logging.info(f"[🗸] Successfully saved {name}")
            except TypeError:
                logging.error(
                    f"[-] Error while saving [ {name} ], Please check the values of your data"
                )
            return data

        return wrapper

    return decorator


def Excel(filename: str, headers: List[str] = None, sheet_name: str = None):
    """
    Convert data to excel file.

    :param filename: Name of the file
    :param headers: Column name
    :param sheet_name: Name of sheet
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, *kwargs)
            wb = Workbook()
            page = wb.active
            name = f"{filename}.xlsx"

            if headers:
                page.append(headers)
            if sheet_name:
                page.title = sheet_name

            try:
                create_files_folder()
                for value in data:
                    page.append(value)
                filepath = get_file_path(name)
                wb.save(filepath)
                logging.info(f"[🗸] Successfully saved {name}")
            except TypeError:
                logging.error(
                    f"[-] Error while saving [ {name} ], "
                    "Please check the values of your data"
                )
            except PermissionError:
                logging.warning(
                    f"[x] Error while saving [ {name} ], "
                    "Please close the file before adding new data"
                )
            return data

        return wrapper

    return decorator


def Json(filename: str, keys: List[str] = None):
    """
    Convert data to json file.

    :param filename: Name of the file
    :param keys: Keys for each value
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, *kwargs)
            if not data:
                return

            name = f"{filename}.json"
            mapped_values = []
            if not keys:
                logging.error(f"[x] Please provide valid keys")
                return

            try:
                for rows in data:
                    dictionary = dict(zip(keys, rows))
                    mapped_values.append(dictionary)
                json_data = json.dumps(mapped_values, indent=4)
                create_files_folder()
                filepath = get_file_path(name)

                with open(filepath, "w", encoding="utf-8") as json_file:
                    json_file.write(json_data)

                logging.info(f"[🗸] Successfully saved {name}")
            except IOError:
                logging.error(
                    f"[-] Error while saving [ {name} ], Please check the values of your data"
                )
            return data

        return wrapper

    return decorator
