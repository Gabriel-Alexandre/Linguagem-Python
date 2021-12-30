from selenium.webdriver import Firefox, Chrome, ChromeOptions
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep

# Quando as ações de click() ou send_keys() não são executadas, o motivo pode ser:
#   1- A janela do driver não é grande o suficiente para mostrar a informação.
#       - Nesse caso, é só alterar o tamanho da janela com o "ChromeOptions".
#   2- Os elementos a serem clicados ou preenchidos ainda não foram carregados.
#       - Nesse caso, posso usar as funções de "WebDriverWait" e "EC" para esperar o carregamento do elemento
#       para que assim que o elemento for carregado, as instruções sejam executadas corretamente.

# -> O código a baixo contém exemplos de implementação para as duas situações.
# -> O código a baixo contém exemplos de busca de elementos usando find_element(By.XPATH, str) e find_element_by_xpath(str).
#   - É importante saber que as funções find_element_by_* estão depreciadas, então não é indicado utilizar.


url = 'https://www.busuu.com/pt/hello'

chrome_options = ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option('useAutomationExtension', False)
browser = Chrome(options=chrome_options)

# Faz requisição para a página.
browser.get(url)
# Encontra elemento e pega atributo.
# login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a')))
# login.get_attribute('href')
login = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a').get_attribute('href')
# login = browser.find_element_by_xpath('/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a').get_attribute('href')
# Encontra elemento e clica.
# button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a')))
# button.click()
browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a').click()
# browser.find_element_by_xpath('/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a').click()
# Faz requisição para a próxima página.
browser.get(login)
# Escreve no input de login.
browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/section/div[1]/form/div[2]/div[1]/input').send_keys("IssoEhUmTeste")
# browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/section/div[1]/form/div[2]/div[1]/input').send_keys("IssoEhUmTeste")

sleep(1)

browser.quit()