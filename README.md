# Data Converter

## About the project

Converts your 2d array into csv, json, and excel file.

## Installation

1. Clone the repo.

- `git clone https://github.com/reny-pacheco/data-converter.git`

2. Go to projects folder.

- `cd data-converter`

3. Create virtual environment. (make sure virtualenv is installed)

- windows: `virtualenv <your_env>`
- linux: `virtualenv -p /usr/bin/python3 <your_env>`

4. Activate your virtual environment.

- windows: `<your_env>\Scripts\activate`
- linux: `source <your_env>/bin/activate`

5. Install requirements.

- `pip install -r requirements.txt`

### Sample data is from [Regions of the Philippines wikipedia page](https://en.wikipedia.org/wiki/Regions_of_the_Philippines 'Regions of the Philippines')

After you installed all the requirements, run `python app.py`

It will save the data as csv, json, and excel and store them inside `files` folder.

### Saving in a single file format

To save data as json, decorate the `get_data` function with `@Json` and add the required arguments. Then run the `app.py` using the command `python app.py`

### Example

```python
@Json("ph_regions", keys=['Name', 'Age', 'Location'])
def save_data():
    return get_ph_regions()
```

It will now create a `files` folder containg `ph_regions.json`

## Converting your own data

Your decorated function should always return a 2d array.

### Example

```python
# app.py
from formats.formats import Excel

@Excel("employees", headers=['Name', 'Age', 'Location'], sheet_name='Devs')
def employee_data():
    data = [
        ['John', 22, 'Japan'],
        ['Mike', 45, 'Korea'],
        ['Peter', 19, 'Philippines'],
        ['Kim', 28, 'Thailand'],
        ['Mae', 47, 'Vietnam'],
    ]
    return data

if __name__ == "__main__":
    employee_data()
```

After you run the file, there is now `employees.xlsx` inside files folder with contents similar to the image below.

![Alt](/images/employees.png 'Title')
