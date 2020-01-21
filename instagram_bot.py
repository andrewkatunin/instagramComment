from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException , StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("URL")

# finds the login button
log_but = ui.WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Log In"]')))

# clicks the login button
log_but.click()


log_but_facebook = ui.WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'KPnG0')))
log_but_facebook.click()


usern = driver.find_element_by_id("email")
#
# # sends the entered username
usern.send_keys("YOUR_EMAIL")
#
# # finds the password box
passw = driver.find_element_by_id("pass")
#
# # sends the entered password
passw.send_keys("YOUR_PASSWORD")
#
# # finds the login button
#login_face = driver.find_element_by_id("loginbutton")
login_face =  ui.WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginbutton")))
login_face.click()  # clicks the login button


#pic = driver.find_element_by_class_name("_9AhH0")
pic = ui.WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME , "_9AhH0")))
pic.click()
time.sleep(2)

comment_box = ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
driver.execute_script("arguments[0].scrollIntoView(true);", comment_box)
comment_box.click()
soup = BeautifulSoup(driver.page_source, features="html.parser")
elems = soup.find_all("a", class_="FPmhX")
already_exist = False
for elem in elems:
    if "YOUR_USERNAME" == elem.text:
        already_exist = True
if not already_exist:
    try:
        comment_box.send_keys("YOUR_COMMENT")
    except(StaleElementReferenceException):
        comment_box = ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
        comment_box.send_keys("YOUR_COMMENT")
    #
    #
    post_butt = ui.WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Post"]')))
    post_butt.click()
driver.close()