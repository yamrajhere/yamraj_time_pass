# pip install selenium requests json

import json
from urllib.parse import quote
from urllib.parse import urlencode

import requests
from requests.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import main_fund

profile_id = "da3ca895-ca86-4e76-910c-7e94a64c85ab"


#### Running the profile:
#### Running the profile:
#### Running the profile:
#### Running the profile:

host = '127.0.0.1'
api_key = 'd7408bb8-7aa3-44c8-baf1-5cdcb1bba371'
config = {
    'headless': False,  # support: true or false
    'autoClose': True,
}
query = urlencode({
    'x-api-key': api_key,  # required
    'config': quote(json.dumps(config))
})
url = f'http://{host}:8848/devtool/launch/{profile_id}?{query}'
print('devtool url: ' + url)
port = main_fund.get_debugger_port(url)
debugger_address = f'{host}:{port}'
print("debugger_address: " + debugger_address)
main_fund.exec_selenium(debugger_address)
url = f'http://{host}:8848/devtool/launch?{query}'
print('devtool url: ' + url)

port = main_fund.get_debugger_port(url)
debugger_address = f'{host}:{port}'
print("debugger_address: " + debugger_address)



#### Selenium work starts from here:
#### Selenium work starts from here:
#### Selenium work starts from here:
#### Selenium work starts from here:
#### Selenium work starts from here:
#### Selenium work starts from here:


options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", debugger_address)


service = ChromeService()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.imdb.com/chart/top")

movies = driver.find_elements(By.CSS_SELECTOR, "li.cli-parent")
for row in movies:
  title = row.find_element(By.CLASS_NAME, 'ipc-title-link-wrapper') # get title
  year = row.find_element(By.CSS_SELECTOR, 'span.cli-title-metadata-item') # get created year
  rate = row.find_element(By.CLASS_NAME, 'ipc-rating-star') # get rate

  move_item = {
    "title": title.text,
    "year": year.text,
    "rate": rate.text
  }
  print(move_item)

movies = driver.find_elements(By.CSS_SELECTOR, "li.cli-parent")
movies_info = []
for row in movies:
  title = row.find_element(By.CLASS_NAME, 'ipc-title-link-wrapper')
  year = row.find_element(By.CSS_SELECTOR, 'span.cli-title-metadata-item')
  rate = row.find_element(By.CLASS_NAME, 'ipc-rating-star')

  move_item = {
    "title": title.text,
    "year": year.text,
    "rate": rate.text
  }
  movies_info.append(move_item)
# create the json file
json_file = open("movies.json", "w")
# convert movies_info to JSON
json.dump(movies_info, json_file)
# release the file resources
json_file.close()
