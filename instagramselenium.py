from selenium import webdriver
import time

#CHANGE Firefox() ACCORDING TO YOUR DRIVER
browser = webdriver.Firefox()

browser.get("https://www.instagram.com")
time.sleep(5)

#RIGHT CLICK TO THE ELEMENT -> INSPECT -> COPY XPATH OR NAME ACCORDING
#TO YOUR CHOICE AND HOW THE ELEMENT IS SUBJECT TO CHANGE.
loginbutton = browser.find_element("xpath", "//*[@id='loginForm']/div/div[3]")
enter_username = browser.find_element("name","username")
password = browser.find_element("name","password")

#CHANGE USERNAME AND PASSWORD WITH YOUR CREDENTIALS.
enter_username.send_keys("<your username>")
password.send_keys("<your password>")

time.sleep(5)
loginbutton.click()
time.sleep(10)


#IF YOU DON'T WANT TO CLOSE YOUR BROWSER, DELETE THIS LINE OF CODE:
browser.close()
