"""
Command Line Emailer
Write a program that takes an email address and string of text on the
command line and then, using selenium, logs in to your email account
and sends an email of the string to the provided address. (You might
want to set up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs.
 You could also write a similar program to send messages from
a Facebook or Twitter account.


@author Sharaf Qeshta
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys

recipient_email = sys.argv[1]
email_body = sys.argv[2]
sender_email_address = "your email"
sender_email_password = "your email password"

browser = webdriver.Chrome()
browser.get('http://mail.google.com')
login_input = browser.find_element(By.ID, 'identifierId')
login_input.send_keys(sender_email_address)
next_button = browser.find_element(By.ID, "identifierNext")
next_button.click()
time.sleep(5)
password_input = browser.find_element(By.NAME, "password")
password_input.send_keys(sender_email_password)
password_next_button = browser.find_element(By.ID, "passwordNext")
password_next_button.click()
root_element = browser.find_element(By.TAG_NAME, 'html')
root_element.send_keys('c')
root_element.send_keys(Keys.TAB)
root_element.send_keys(recipient_email)
root_element.send_keys(Keys.TAB)
root_element.send_keys(Keys.TAB)
root_element.send_keys(email_body)
root_element.send_keys(Keys.ENTER)

print("email sent.")
