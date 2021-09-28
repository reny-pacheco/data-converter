from save_data import SaveToExcel, SaveAsCsv


# save data as .xlsx file
class MyScraperExcel(SaveToExcel):
    def __init__(self, filename, url):
        super().__init__(filename, url)

    def __call__(self):
        self.save(headers=['Job Title', 'Salary (PHP)'], sheet_name='Web Developer Jobs')

    """
    you can override the get_data function to return your specified data,
    must return a 2d list
    
    def get_data(self):
        return [['Tom', 'Cat'], ['Jerry', 'Mouse']
        
    """

    """
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


if __name__ == "__main__":
    url = 'https://ph.indeed.com/nursing-jobs'
    # url = 'https://ph.indeed.com/web-developer-jobs'

    scrape_and_save = MyScraperCsv(filename="nursing_jobs", url=url)
    # scrape_and_save = MyScraperExcel(filename="nursing_jobs", url=url)

    scrape_and_save()
