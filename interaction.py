from selenium import webdriver
from selenium.webdriver.common.keys import Keys
URL = "http://secure-retreat-92358.herokuapp.com/"


chrome_driver_path = "/home/hiren/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

fname = driver.find_element_by_name("fName")

fname.send_keys("Hiren")
lname = driver.find_element_by_name("lName")
lname.send_keys("Patel")
email = driver.find_element_by_name("email")
email.send_keys(")

sign_up = driver.find_element_by_css_selector(".btn-primary")
sign_up.send_keys(Keys.ENTER)

