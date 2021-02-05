from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
username = 'unitedbrun'
password = 'thisisme'
driver.get("http://www.twitter.com/login")
time.sleep(5)
for x in driver.find_elements_by_tag_name("input"):
    print(x.get_property("name"))
username_input, password_input = driver.find_elements_by_tag_name("input")[-2:]
username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
search_username = input("Username of the person you're looking for?\n@")
driver.get(f"http://www.twitter.com/{search_username}/following")
main = driver.find_element_by_tag_name("main")
for x in range(10):
    time.sleep(3)
    main.send_keys(Keys.END)
time.sleep(5)
junk = driver.find_elements_by_tag_name("span")
for x in junk:
    print(x.text)
# arr = junk.split("@")
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
