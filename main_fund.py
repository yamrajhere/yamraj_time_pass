import requests
from requests.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


# get_debugger_port: Get the debugger port
def get_debugger_port(url: str):
    try:
        resp = requests.get(url).json()
        if resp['data'] is None:
            raise Exception(resp['msg'])
        port = resp['data']['port']
        return port
    except HTTPError:
        raise Exception(HTTPError.response)


def exec_selenium(debugger_address: str):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", debugger_address)
    # Replace with the corresponding version of WebDriver path.
    chrome_driver_path = r'your webdriver path'
    service = ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://nstbrowser.io")
    driver.save_screenshot('screenshot.png')
    driver.close()
    driver.quit()