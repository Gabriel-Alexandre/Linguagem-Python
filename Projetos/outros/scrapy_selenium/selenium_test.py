from selenium.webdriver import Firefox
from time import sleep

url = 'https://www.busuu.com/pt/hello'

browser = Firefox()

# Faz requisição para a página.
browser.get(url)
# Encontra elemento e pega atributo.
login = browser.find_element_by_xpath('/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a').get_attribute('href')
# Encontra elemento e clica.
browser.find_element_by_xpath('/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a').click()
# Faz requisição para a próxima página.
browser.get(login)
# Escreve no input de login.
browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/section/div[1]/form/div[2]/div[1]/input').send_keys("IssoEhUmTeste")

sleep(1)

browser.quit()