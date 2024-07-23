from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import resources

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

driver.get(resources.url)

def click_xpath(element):
    try:
        xpath = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        xpath.click()
    except:
        driver.quit()

sign_on = '//*[@id="ssoBtn"]'
click_xpath(sign_on)

