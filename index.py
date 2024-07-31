from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import resources

resources.email = input('email: ')
resources.password= input('senha: ')

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

def write_enter_xpath(element, text):
    try:
        text = str(text)
        xpath = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        xpath.send_keys(text)
        time.sleep(1)
        xpath.send_keys(Keys.ENTER)
    except:
        driver.quit()

df = pd.read_excel('planilha_padrao_julius.xlsx')


sign_on_btn = '//*[@id="ssoBtn"]'
click_xpath(sign_on_btn)

field_email = '//*[@id="i0116"]'
write_xpath(field_email, resources.email)

avancar_btn = '//*[@id="idSIButton9"]'
click_xpath(avancar_btn)

field_password = '//*[@id="passwordInput"]'
write_xpath(field_password, resources.password)

entrar_btn = '//*[@id="submitButton"]'
click_xpath(entrar_btn)

nao_btn = '//*[@id="idBtn_Back"]'
click_xpath(nao_btn)

time.sleep(3)
contas_pagar_btn = '//*[@id="groupNode_payables"]'
click_xpath(contas_pagar_btn)

pagamentos_btn = '//*[@id="itemNode_payables_payables_payments"]'
click_xpath(pagamentos_btn)

time.sleep(2)
folha_btn = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:_FOTsdi__PaymentLanding_itemNode__FndTasksList::icon"]'
click_xpath(folha_btn)

time.sleep(2)
gerenciar_link = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:_FOTRaT:0:RAtl23"]'
click_xpath(gerenciar_link)

for row in df.index:

    dados = {
    'bu': str(df.loc[row, 'bu']),
    'cnpj': str(df.loc[row,'fornecedor']),
    'emissao': df.loc[row, 'competencia'],
    'num_doc': str(df.loc[row,'num_doc']),
    'cod_barras': str(df.loc[row,'digitavel']),
    'venc': str(df.loc[row,'vencimento']),
    'valor': str(df.loc[row,'valor']),
    'agencia': str(df.loc[row, 'agencia'])    
    }        

    adicionar_btn = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:1:pt1:panelGroupLayout2:AT1:_ATp:create"]/a'
    click_xpath(adicionar_btn)

    field_bu = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:fcslov1:sis1:is1::content"]'
    write_enter_xpath(field_bu, dados['bu'])

    field_num_doc = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:it18::content"]'
    write_enter_xpath(field_num_doc, dados['num_doc'])

    field_emissao = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:id13::content"]'
    driver.find_element(By.XPATH, field_emissao).clear()
    write_enter_xpath(field_emissao, dados['emissao'])

    field_venc = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:id9::content"]'
    write_enter_xpath(field_venc, dados['venc'])

    field_cod_barras = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:it39::content"]'
    cod_barras = resources.formatar_cod_barras(dados['cod_barras'])
    write_enter_xpath(field_cod_barras, cod_barras)

    time.sleep(1)
    field_valor = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:it15::content"]'
    valor_verificar = driver.find_element(By.XPATH, field_valor).get_property('value')
    dados['valor'] = dados['valor'].replace('.', ',')
    valor_validado = resources.validador_valor(valor_verificar, dados['valor'])

    if valor_validado:
        field_cnpj = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:vendorRegistration1Id::content"]'
        cnpj = resources.formatar_cnpj(dados['cnpj'])
        write_enter_xpath(field_cnpj, cnpj)
        
        xpath_agencia = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:bankBranchNameId::content"]'
        field_agencia = driver.find_element(By.XPATH, xpath_agencia)
        agencia = resources.formatar_agencia(dados['agencia'])
        field_agencia.send_keys(agencia)
        time.sleep(1)
        field_agencia.send_keys(Keys.TAB)

        time.sleep(1)
        xpath_agencia_check = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:it11"]'
        agencia_check = driver.find_element(By.XPATH, xpath_agencia_check).text

        if agencia in agencia_check:
            print('cheked')
            corresponder_btn = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:AT3:_ATp:ctb1"]/a'
            click_xpath(corresponder_btn)

            corresponder_sim_btn = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:cb2"]'
            click_xpath(corresponder_sim_btn)

            time.sleep(2)
            xpath_nf_correspondida = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:AT3:_ATp:ATt3::db"]'
            nf_correspondida = driver.find_element(By.XPATH, xpath_nf_correspondida).text

            if nf_correspondida == 'Nenhum dado a ser exibido.':
                print('deu merda')
                cancelar_bnt = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:SPc"]'
                click_xpath(cancelar_bnt)

                cancelar_sim_btn = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:cancelcommandButton4"]'    
                click_xpath(cancelar_sim_btn)

                continue

            else:
                xpath_nf_validar = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:AT3:_ATp:ATt3::db"]/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]'
                time.sleep(2)
                nf_validar = driver.find_element(By.XPATH, xpath_nf_validar).text

                if dados['num_doc'] in nf_validar:
                    print('to aqui')
                    
                    xpath_salvar = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:APsv2"]'
                    click_xpath(xpath_salvar)

                    time.sleep(2)
                    xpath_corresdencia_exata = '//*[@id="pt1:_FOr1:1:_FOSritemNode_payables_payables_payments:0:MAnt2:2:pt1:AP1:soc3::content"]'
                    corresdencia_exata = driver.find_element(By.XPATH, xpath_corresdencia_exata)
                    print(corresdencia_exata)
        else:
            print('Agencia invalida')
            driver.quit()

    else:
        driver.quit()