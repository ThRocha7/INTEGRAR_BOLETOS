from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

def click_xpath(element):
    try:
        xpath = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        xpath.click()
    except:
        driver.quit()

service = Service()
options = webdriver.ChromeOptions()
chrome_prefs = {
            "profile.default_content_settings.popups": 0,
            "download.prompt_for_download": True,
            "plugins.always_open_pdf_externally": True
        }
options.add_experimental_option("prefs", chrome_prefs)
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://fa-evvi-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/FuseWelcome?_adf.ctrl-state=gknd33cp2_687&_afrLoop=11190830558773601&_afrWindowMode=0&_afrWindowId=null&_afrFS=16&_afrMT=screen&_afrMFW=1422&_afrMFH=612&_afrMFDW=1280&_afrMFDH=720&_afrMFC=8&_afrMFCI=0&_afrMFM=0&_afrMFR=129&_afrMFG=0&_afrMFS=0&_afrMFO=0')

sign_on = '//*[@id="ssoBtn"]'
click_xpath(sign_on)
