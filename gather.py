import requests
import logging
import re
from time import sleep
from bs4 import BeautifulSoup as Bs

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


class InitBS:
    def __init__(self, url):
        self.url = url

        # checking if the url is valid
        try:
            logging.info(f'[+] Connecting to {self.url}')
            sleep(2)

            source = requests.get(self.url).text

            logging.info(f'[+] Successful request to {self.url}')
            sleep(2)

            self.soup = Bs(source, 'lxml')

        except requests.exceptions.SSLError:
            logging.debug(f'[x] Error while requesting the webpage from {self.url}, '
                          f'Please check the url!!!')
            self.soup = None

        except requests.exceptions.ConnectionError:
            logging.debug(f'[x] Unable to connect to {self.url},'
                          f'Please check the url!!!')
            self.soup = None


class Gather(InitBS):
    def __init__(self, url):
        super().__init__(url)

    # def get_data(self):
    #     """
    #     Get the data from a web page (Indeed.com)
    #     :return: 2d list containing the data
    #     """
    #
    #     if self.soup is None:
    #         return None
    #
    #     job = []
    #     jobs = []
    #
    #     job_divs = self.soup.find_all('td', class_='resultContent')
    #
    #     for job_div in job_divs:
    #         job_title_h2 = job_div.find('h2', class_='jobTitle')
    #         job_title = job_title_h2.find_all('span')[-1].text
    #         job_salary_div = job_div.find('div', class_='salary-snippet-container')
    #
    #         if job_salary_div is None:
    #             job_salary = 'Not Available'
    #
    #         else:
    #             job_salary = job_salary_div.span.text
    #             job_salary = re.sub(r'\s*PHP\s*', "", job_salary, re.I | re.U | re.S)
    #
    #         job.append(job_title)
    #         job.append(job_salary)
    #
    #         jobs.append(job)
    #         job = []
    #
    #     logging.info(f'[+] Successfully get data from {self.url}')
    #
    #     return jobs

    # Get Philippine regions from wikipedia website
    def get_data(self):
        if self.soup is None:
            return None

        region = []
        regions = []

        table_data = self.soup.find('table', class_="wikitable")
        table_body = table_data.find('tbody')
        table_rows = table_body.find_all('tr')[1:]

        for table_row in table_rows[:-1]:
            lgus = []
            td = table_row.find('td')
            td_values = table_row.find_all('td')

            region_name = td.find('a').text

            island_group = td_values[2].text.strip()
            region_center = td_values[3].text.strip()
            lgu_td = td_values[4]

            population = td_values[6].text.strip()
            population = re.sub('\(.*', '', population, re.I)
            population = re.sub(',', '', population, re.I)
            population = int(population)

            land_area = td_values[5].text.strip()
            land_area = re.sub(r'\s*(km\d?.*)', ' km squared', land_area, re.I)

            lgu_lists = lgu_td.find_all('li')
            for lgu_list in lgu_lists:
                lgus.append(lgu_list.find('a').text)

            lgu_str = ', '.join(lgu for lgu in lgus)

            region.append(region_name)
            region.append(island_group)
            region.append(region_center)
            region.append(population)
            region.append(land_area)
            region.append(lgu_str)

            regions.append(region)
            region = []

        logging.info(f'[+] Successfully get data from {self.url}')

        return regions
