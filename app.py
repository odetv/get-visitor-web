from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_path = 'chromedriver/chromedriver.exe'
url = 'URL_WEB_TARGET'

service = Service(driver_path)

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

try:
    for i in range(5650):
        print(f"Reloading {i+1}")
        sleep(1)
        driver.refresh()
finally:
    driver.quit()
