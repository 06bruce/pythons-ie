from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

# you can take any valid username
audience = [ 'sundarpichai','virat.kholi','rudymancuso']
message = "testing of a bot"

class bot:

	def __init__(self, username, password, audience, message):
	
		# initializing the username
		self.username = username
		
		# initializing the password
		self.password = password
		
		# passing the list of user or initializing
		self.user = user
		
		# passing the message of user or initializing
		self.message = message
		
		# initializing the base url.
		self.base_url = 'https://www.instagram.com/'
		
		# here it calls the driver to open chrome web browser.
		self.bot = driver
		
		# initializing the login function we will create
		self.login()
def self(login):

	self.bot.get(self.base_url)
	
	# ENTERING THE USERNAME FOR LOGIN INTO INSTAGRAM
	enter_username = WebDriverWait(self.bot, 20).until(
		expected_conditions.presence_of_element_located((By.NAME, 'username')))

	enter_username.send_keys(self.username)
	
	# ENTERING THE PASSWORD FOR LOGIN INTO INSTAGRAM
	enter_password = WebDriverWait(self.bot, 20).until(
		expected_conditions.presence_of_element_located((By.NAME, 'password')))
	enter_password.send_keys(self.password)

	# RETURNING THE PASSWORD and login into the account
	enter_password.send_keys(Keys.RETURN)
	time.sleep(5)
 
# first pop-up box
self.bot.find_element_by_xpath(
	'//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)

# 2nd pop-up box
self.bot.find_element_by_xpath(
	'/html/body/div[4]/div/div/div/div[3]/button[2]').click()

time.sleep(4)
# this will click on message(direct) option.
self.bot.find_element_by_xpath(
	'//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()

time.sleep(3)

for i in user:

	# enter the username
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
	time.sleep(2)

	# click on the username
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[2]/div[2]/div').click()
	time.sleep(2)

	# next button
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[1]/div/div[2]/div/button').click()
	time.sleep(2)

	# click on message area
	send = self.bot.find_element_by_xpath(
		'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

	# types message
	send.send_keys(self.message)
	time.sleep(1)

	# send message
	send.send_keys(Keys.RETURN)
	time.sleep(2)

	# clicks on pencil icon
	self.bot.find_element_by_xpath(
		'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
	time.sleep(2)
	# here will take the next username from the user's list.

def init():

	# you can even enter your personal account.
	bot('username', 'password', 'user', 'message')
	input("DONE")

# calling this function will message everyone's
# that is on your user's list...:)
init()

