# importing modules
import requests
import os

URL = "https://visualisations.aemo.com.au/aemo/data/NEM/SEVENDAYOUTLOOK/WEB_SEVENDAY_OUTLOOK.CSV"

# fetching data from aemo
res = requests.get(URL)

# extracting required data from the response object
data = res.text

csv_path = os.path.abspath(__file__)
csv_path = f'{os.sep.join(csv_path.split(os.sep)[:-1])}{os.sep}7_day_outlook.csv'

print(csv_path)

# writing data to a file
with open(csv_path, "w") as data_file:
    data_file.write(data)
