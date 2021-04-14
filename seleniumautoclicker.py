from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("")
for x in driver.find_elements_by_class_name("icon"):
    x.click()
    time.sleep(1)
