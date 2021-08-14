from prompt_toolkit.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time


driver = webdriver.Chrome(
    executable_path='D:\Work stuff\Second year\First semester\Software QA\QA_Resit_August\chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/login')

search = driver.find_element(By.ID, 'username')
search.send_keys('tomsmith')
search = driver.find_element(By.ID, 'password')
search.send_keys('SuperSecretPassword!')

element = driver.find_element_by_css_selector('.fa.fa-2x.fa-sign-in')
search.send_keys(Keys.ENTER)

time.sleep(5)
driver.close()

