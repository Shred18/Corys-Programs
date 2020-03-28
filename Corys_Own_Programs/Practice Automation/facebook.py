#This will log you into facebook
##Helpful References - https://stackoverflow.com/questions/38684175/how-to-click-allow-on-show-notifications-popup-using-selenium-webdriver


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#To bypass the allow/deny web notifications pop up
option = Options()
option.add_argument("--disable-notifications")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1 }) #1 will allow, 2 will deny the pop up
driver = webdriver.Chrome(options=option,executable_path = '/Users/coryshreffler/Desktop/Python/Corys_Own_Programs/Practice Automation/chromedriver')
#driver.implicitly_wait(50) #this will allow the script to keep looking for the element, and not quit until its done so for 30 seconds and hasnt found anything
fb = driver
fb.implicitly_wait(50)
fb.get('https://facebook.com') #takes you to facebook

username = fb.find_element_by_xpath('//*[@id="email"]') #finds the username box (get this by inspecting the page)
username.send_keys('Coryshreffler32@gmail.com') #sends your user name to the username box
password = fb.find_element_by_xpath('//*[@id="pass"]') #'
password.send_keys('ROFL U WISH')#'
login = fb.find_element_by_xpath('//*[@id="u_0_b"]')#Finds the login button
login.click() #executes the button

marketplace = fb.find_element_by_xpath('//*[@id="navItem_1606854132932955"]/a/div') #finds marketplace button
marketplace.click() #executes marketplace button

time.sleep(5) #delays execution of the script by the amount in parenthesis
sellsomething = fb.find_element_by_xpath('//*[@id="facebook"]/body/div[1]/div[3]/div[1]/div/div/div[1]/div/div/div/button')
sellsomething.click()

time.sleep(7)
itemforsale = fb.find_element_by_xpath('//*[@id="facebook"]/body/div[6]/div[2]/div/div/div/div/div[2]/div/div[1]/a/span ')
time.sleep(4)
itemforsale.click()

time.sleep(3)
wutusell = fb.find_element_by_xpath('//*[@id="rc.js_55"]/div/div[1]/div[1]/div[1]/label/input')
time.sleep(5)
wutusell.send_keys('New Ndur Bluetooth Smartwatch')


#price = fb.find_element_by_xpath('//*[@id="rc.js_55"]/div/div[1]/div[2]/div[1]/label/input')
#time.sleep(3)
#price.send_keys(60)







