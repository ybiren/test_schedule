from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
  
    return webdriver.Chrome(options=options)



fileToWrite = open("dd.txt", "w", encoding="utf-8")
#now = datetime.now()
#str = now.strftime('%Y-%m-%d %H:%M:%S')
#fileToWrite.write(str)  

driver = initSeleniumDriver()
driver.get("https://apps.land.gov.il/MichrazimSite/#/homePage")
enterBtn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "button-enter")))
# Print the page source
fileToWrite.write(driver.page_source)

#enterBtn.click()
fileToWrite.close()
driver.quit()

    
