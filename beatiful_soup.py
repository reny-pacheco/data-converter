import requests
import logging

from bs4 import BeautifulSoup as Bs


logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)


class BS:
    def __init__(self, url):
        self.url = url

    def get_soup(self):
        # checking if the url is valid
        try:
            source = requests.get(self.url).text
            logging.info(f"[+] Connecting to {self.url}")
            return Bs(source, "lxml")

        except requests.exceptions.SSLError:
            logging.debug(
                f"[x] Error while requesting the webpage from {self.url}, "
                f"Please check the url!!!"
            )
            return None

        except requests.exceptions.ConnectionError:
            logging.debug(
                f"[x] Unable to connect to {self.url},"
                f"Please check the url!!!"
            )
            return None
