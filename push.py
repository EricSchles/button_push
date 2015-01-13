# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("web_address")
parser.add_argument("element_id")
args = parser.parse_args()

web_address = args.web_address
element_id = args.element_id

driver = webdriver.Firefox()

driver.get(web_address)
elem = driver.find_element_by_id(element_id)
elem.click()

driver.close()