import re
import logging
from beatiful_soup import BS

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)

def get_ph_regions():
    url = "https://en.wikipedia.org/wiki/Regions_of_the_Philippines"
    soup = BS(url).get_soup()

    if soup is None:
        logging.error(f"[-] Error occured, File not saved.")
        return None

    region = []
    regions = []

    try:
        table_data = soup.find("table", class_="wikitable")
        table_body = table_data.find("tbody")
        table_rows = table_body.find_all("tr")[1:]

        for table_row in table_rows[:-1]:
            lgus = []
            td = table_row.find("td")
            td_values = table_row.find_all("td")

            region_name = td.find("a").text
            region_name_number = td.find("span").text.strip()
            region_name_number = re.sub("(\(|\))", "", region_name_number)

            island_group = td_values[2].text.strip()
            region_center = td_values[3].text.strip()
            lgu_td = td_values[4]

            population = td_values[6].text.strip()
            population = re.sub("\(.*", "", population, re.I)
            population = re.sub(",", "", population, re.I)
            population = int(population)

            land_area = td_values[5].text.strip()
            land_area = re.sub(r"\s*(km\d?.*)", " km squared", land_area, re.I)

            lgu_lists = lgu_td.find_all("li")
            for lgu_list in lgu_lists:
                lgus.append(lgu_list.find("a").text)

            lgu_str = ", ".join(lgu for lgu in lgus)

            region.append(region_name)
            region.append(region_name_number)
            region.append(island_group)
            region.append(region_center)
            region.append(population)
            region.append(land_area)
            region.append(lgu_str)

            regions.append(region)
            region = []

        logging.info(f"[+] Successfully extracted data")

        return regions
    except:
        logging.info(f"[-] Error while extracting data")
        return None