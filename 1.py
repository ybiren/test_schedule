from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException

fileToWrite = open("dd.txt", "a", encoding="utf-8")
now = datetime.now()
str = now.strftime('%Y-%m-%d %H:%M:%S')
fileToWrite.write(str)  
fileToWrite.close()
