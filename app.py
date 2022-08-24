
from convert import Convert
from beatiful_soup import BS

from examples.ph_regions import get_data

keys = keys = [
    "Region Name",
    "Region",
    "Island Group",
    "Region Center",
    "Population",
    "Land Area",
    "Local Goverments",
]


@Convert("new_ph_data.json",keys=keys)
@Convert("new_ph_data.xlsx", headers=keys, sheet_name="Philippine Regions")
def save_data():
    url = "https://en.wikipedia.org/wiki/Regions_of_the_Philippines"
    soup = BS(url).get_soup()
    return get_data(soup)


if __name__ == "__main__":
    save_data()
