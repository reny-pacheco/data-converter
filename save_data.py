from openpyxl import Workbook
from gather import Gather
from time import sleep
import logging
import csv
import os

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


# creating files folder
def create_files_folder():
    if not os.path.exists('files'):
        logging.info("[x] Creating [ files ] folder")
        os.makedirs('files')
        sleep(2)


# save data as .xlsx file
class SaveToExcel(Gather):
    def __init__(self, filename, url):
        self.filename = filename
        super().__init__(url)

    def save(self, data=None, headers=None, sheet_name=None):
        """
        Save the data to xlsx file format

        :param data: 2d list containing values
        :param headers: type(list) Column Headers ['Name', 'Age', 'Location']
        :param sheet_name: type(string) Sheet Name
        """

        if self.soup is None:
            logging.error(f"[x] No data is saved, Please check the url: {self.url}")
            return None

        wb = Workbook()
        page = wb.active

        # if data is none, get the data  using the get_data function from
        # Gather class,
        # If data is not None, use and save the data specified by the user
        data = data if data is not None else self.get_data()
        filename = f'{self.filename}.xlsx'

        sleep(2)

        # include the source url to the file
        page.append(['Source', self.url])
        page.append(['', ''])

        if headers:
            page.append(headers)

        if sheet_name:
            page.title = sheet_name

        try:
            create_files_folder()

            for value in data:
                page.append(value)

            wb.save('./files/' + filename)

            logging.info(f'[+] Successfully saved {filename}')

        except TypeError:
            logging.error(f'[x] Error while saving [ {filename} ], Please check the values of your data')

        except PermissionError:
            logging.warning(f"[x] Error while saving [ {filename} ], Please close the file before adding new data")


# save data as .csv file
class SaveAsCsv(Gather):
    def __init__(self, filename, url):
        self.filename = filename
        super().__init__(url)

    def save(self, data=None, headers=None):
        filename = f'{self.filename}.csv'
        create_files_folder()

        csv_file = open('./files/' + filename, 'w', newline='')
        csv_writer = csv.writer(csv_file)

        if headers is not None:
            csv_writer.writerow(headers)

        data = data if data is not None else self.get_data()

        try:
            for values in data:
                csv_writer.writerow(values)

            csv_file.close()

            logging.info(f'[+] Successfully saved {filename}')

        except TypeError:
            logging.error(f'[x] Error while saving [ {filename} ], Please check the values of your data')
