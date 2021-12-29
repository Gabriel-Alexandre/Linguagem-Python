from selenium.webdriver import Firefox
from time import sleep

url = "https://www.busuu.com/pt/logout"

browser = Firefox()

print("Browser1: ", browser)

browser.get(url)
a = browser.find_element_by_xpath('//*[@id="main-wrapper"]/div[1]/header/nav/div/div[1]/div[4]/a')

print("Browser1: ", browser)
print("a: ", a)

# a.find_element_by_xpath('//*[@id="google-authentication"]').click()

# sleep(1)

browser.quit()