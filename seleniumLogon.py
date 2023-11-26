#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
# login 
print("Test case 1: Loging in")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("http://localhost:8069/web/login")
print(driver.title)
#search_bar = driver.find_element_by_name("q")
driver.get("http://localhost:8069/web/login")
print("Able to access the login page")

username = wait.until(EC.visibility_of_element_located((By.NAME, "login")))
username.clear()
username.send_keys("hiyunfengzhao@gmail.com")
print("Able to type user name")

password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password.clear()
password.send_keys("252915967")
print("Able to type password")
password.send_keys(Keys.RETURN)
time.sleep(3)

print("Test case 4: Positive - Register a vehicle")
driver.get("http://localhost:8069/web#cids=1&default_active_id=mail.box_inbox&action=104&menu_id=75&active_id=mail.box_inbox")
time.sleep(3) 
menu_button = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/button/i")
print("Click Menu button")
menu_button.click()
time.sleep(3)  
fleet_button = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div/a[2]")
print("Click Fleet button")
fleet_button.click()
time.sleep(3) 
create_button = driver.find_element(By.XPATH, "//button[@title='Create record']")
print("Click Create button")
create_button.click()
time.sleep(3)
input_area = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[4]/h1/div/div[1]/div/input")
if input_area is not None:
    print("Found input field")
    input_area.send_keys('A1')
else:
    print("Not Found. Closing program.")
    driver.quit() 

time.sleep(3)
save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
print("Click Save button")
save_button.click()
time.sleep(3)  
menu_button = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/button/i")
menu_button.click()
time.sleep(3)  
fleet_button = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div/a[2]")
fleet_button.click()
time.sleep(3) 

registered_section = driver.find_element(By.XPATH, "//span[contains(text(), 'Registered')]/ancestor::div[contains(@class, 'o_kanban_group')]")
entries = registered_section.find_elements(By.XPATH, ".//div[contains(@class, 'oe_kanban_details')]")
audi_a1_present = any("Audi/A1" in entry.text for entry in entries)
if audi_a1_present:
    print("Test Passed: Audi/A1 is present under Registered.")
else:
    print("Test Failed: Audi/A1 is not found under Registered.")
time.sleep(3)

print("Test case 5: Negative - Invalid odometer value") 
audi_a1 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Audi')]")))
audi_a1.click()
print("Click on Audi/A1")
odometer_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Odometer')]")))
odometer_element.click()
print("Click on Odometer")
time.sleep(3)
create_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create')]")
print("Click Create button")
create_button.click()
time.sleep(3)
input_element = driver.find_element(By.CSS_SELECTOR, "input.o_field_float.o_field_number.o_input")
input_element.click()
input_element.send_keys("-1")
print("Input negative value")
save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
save_button.click()
print("Test case 5 failed: Odometer values should never be negative")
time.sleep(3)
