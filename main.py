from save_data import SaveToExcel, SaveAsCsv, SaveAsJson
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


# save data as .xlsx file
class MyScraperExcel(SaveToExcel):
    def __init__(self, filename, url):
        super().__init__(filename, url)

    def __call__(self):
        self.save(headers=['Region Name',
                           'Region',
                           'Island Group',
                           'Region Center',
                           'Population',
                           'Land Area',
                           'Local Goverments'
                           ], sheet_name='Philippine Regions')

    """
    you can override the get_data function to return your specified data,
    must return a 2d list
  
    Or you can add an additional parameter (data) to save function,
    data must be a 2d list
    
    def __call__(self):
        self.save(data=[['Tom', 'Cat'], ['Jerry', 'Mouse']], headers=['Name', 'Species'], sheet_name='Job Listings')
    
    """


class MyScraperCsv(SaveAsCsv):
    def __init__(self, filename, url):
        super().__init__(filename, url)

    def __call__(self):
        self.save(headers=['Job Title', 'Salary (PHP)'])

    """
    Or by using your pre-defined data
    data must be a 2d list
    
    def __call__(self):
        self.save(data=[['Tom', 'Cat'], ['Jerry', 'Mouse']], headers=['Name', 'Species'])
    """


class MyScraperJson(SaveAsJson):
    def __init__(self, filename, url):
        super().__init__(filename, url)

    def __call__(self):
        self.save(key=['Region Name',
                       'Region',
                       'Island Group',
                       'Region Center',
                       'Population',
                       'Land Area',
                       'Local Goverments'
                       ])


if __name__ == "__main__":
    # url = 'https://ph.indeed.com/nursing-jobs'
    # url = 'https://ph.indeed.com/web-developer-jobs'
    url = 'https://en.wikipedia.org/wiki/Regions_of_the_Philippines'

    # scrape_and_save = MyScraperCsv(filename="web_dev_jobs", url=url)
    # scrape_and_save = MyScraperExcel(filename="ph_region_data", url=url)
    scrape_and_save = MyScraperJson(filename="ph_region_data", url=url)
    # scrape_and_save = MyScraperJson(filename="web_dev_jobs", url=url)

    scrape_and_save()
