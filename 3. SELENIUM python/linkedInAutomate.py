import os
try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

except:
	os.system('pip install -- upgrade selenium')

#-----web Driver manager
# from webdriver_manager.chrome import ChromeDriverManager
#============ if you want to use it do install this lib using pip then 
#======== decomment out 
try:
	import time
	import sys
	import random
except:
	os.system('pip install --upgrade time sys random')
	##----- all imports finish


#---- step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb
 
#-----step 1 : open cred.py file in current directory then edit string variables user and passw
from cred import *
# print(user,passw)



# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) 


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
# chrome_options.add_argument('--no-sandbox') # Bypass OS security model
# chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
# chrome_options.add_argument('start-maximized') 
# chrome_options.add_argument('disable-infobars')
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument(f'user-agent={user_agent}')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--allow-running-insecure-content')
# chrome_options.add_argument('--log-level=OFF')

chrome_options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options)



def login(email,password):
	driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
	ss = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[1]/input').send_keys(email)
	driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[2]/input').send_keys(password)
	# print(ss)
	driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
	


def acceptConnections():
	driver.get('https://www.linkedin.com/mynetwork/invitation-manager/?invitationType=CONNECTION')
	
	acceptButtons = []
	
	while len(acceptButtons)==0:
		acceptButtons = driver.find_elements_by_xpath("//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
	
	# Accept connections by clicking the buttons
	for button in acceptButtons:
		button.click()
		time.sleep(2) ##-- 2 seconds


if __name__=="__main__":
	login(user,passw) #----if you're using it for first time then use it for login ##else comment it out
	acceptConnections()
