from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
# login 
driver = webdriver.Chrome()
driver.get("http://localhost:8069/web/login")
print(driver.title)
#search_bar = driver.find_element_by_name("q")
driver.get("http://localhost:8069/web/login")
print("Ning: Step1 passed")
search_bar = driver.find_element(By.NAME, "login")
search_bar.clear()
time.sleep(3)
search_bar.send_keys("yourUsername")
print("Ning: Step2 passed")
time.sleep(3)
search_bar = driver.find_element(By.NAME, "password")
print("Ning: Step3 passed")
time.sleep(3)
search_bar.send_keys("yourPassword")
time.sleep(3)
#search_bar.clear()
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
print(driver.current_url)

# click fleet
driver.get("http://localhost:8069/web#cids=1&default_active_id=mail.box_inbox&action=104&menu_id=75&active_id=mail.box_inbox")
time.sleep(5) 
menu_button = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/button/i")
menu_button.click()
time.sleep(5)  
fleet_button = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div/a[2]")
fleet_button.click()
time.sleep(5) 
create_button = driver.find_element(By.XPATH, "//button[@title='Create record']")
create_button.click()
time.sleep(5)
input_area = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[4]/h1/div/div[1]/div/input")
if input_area is not None:
    print("Found")
    input_area.send_keys('A1')
else:
    print("Not Found. Closing program.")
    driver.quit() 

time.sleep(3)
save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
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
driver.close()


