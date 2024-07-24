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

def write_xpath(element, text):
    try:
        text = str(text)
        xpath = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        xpath.send_keys(text)
    except:
        driver.quit()

sign_on_btn = '//*[@id="ssoBtn"]'
click_xpath(sign_on_btn)

resources.email = input('email: ')
field_email = '//*[@id="i0116"]'
write_xpath(field_email, resources.email)

avancar_btn = '//*[@id="idSIButton9"]'
click_xpath(avancar_btn)

resources.password= input('senha: ')
field_password = '//*[@id="passwordInput"]'
write_xpath(field_password, resources.password)

entrar_btn = '//*[@id="submitButton"]'
click_xpath(entrar_btn)

nao_btn = '//*[@id="idBtn_Back"]'
click_xpath(nao_btn)

contas_pagar_btn = '//*[@id="groupNode_payables"]'
click_xpath(contas_pagar_btn)

pagamentos_btn = '//*[@id="itemNode_payables_payables_payments"]'
click_xpath(pagamentos_btn)

folha_btn = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:_FOTsdi__PaymentLanding_itemNode__FndTasksList::icon"]'
click_xpath(folha_btn)

gerenciar_link = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:_FOTRaT:0:RAtl23"]'
click_xpath(gerenciar_link)

adicionar_btn = '//*[@id="pt1:_FOr1:0:_FOSritemNode_payables_payables_payments:0:MAnt2:1:pt1:panelGroupLayout2:AT1:_ATp:create::icon"]'
click_xpath(adicionar_btn)

field_bu = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:fcslov1:sis1:is1::content"]'
write_xpath(field_bu, '123')

field_num_doc = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:it18::content"]'
write_xpath(field_num_doc, '123')

field_emissao = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:id13::content"]'
write_xpath(field_emissao, '12/01/2024')