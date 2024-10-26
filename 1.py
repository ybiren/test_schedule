from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException

def initSeleniumDriver():
    # Setup Chrome options to run in headless mode
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--log-level=3") # Fatal errors only
    #options.add_argument("--headless")
    options.add_argument("--headless=new")
    #options.add_argument("--disable-gpu")
    options.add_argument("--window-position=-2400,-2400")
  
    #driver_path = r'C:\Users\yossi\.wdm\drivers\chromedriver\win64\127.0.6533.72\chromedriver-win32\chromedriver.exe'
    # Setup WebDriver
    #return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return webdriver.Chrome(options=options)



fileToWrite = open("dd.txt", "a", encoding="utf-8")
now = datetime.now()
str = now.strftime('%Y-%m-%d %H:%M:%S')
fileToWrite.write(str)  
fileToWrite.close()

driver = initSeleniumDriver()

