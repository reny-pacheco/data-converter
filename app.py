from examples.ph_regions import get_ph_regions
from formats.formats import Csv, Excel, Json

keys = [
    "Region Name",
    "Region",
    "Island Group",
    "Region Center",
    "Population",
    "Land Area",
    "Local Goverments",
]


@Csv("ph_regions", headers=keys)
@Json("ph_regions", keys=keys)
@Excel("ph_regions", headers=keys, sheet_name="Regions of the Philippines")
def save_data():
    return get_ph_regions()


if __name__ == "__main__":
    save_data()
