import scrapy
# from scrapy.http.request import Request
from scrapy.utils.project import get_project_settings
from selenium.webdriver import Firefox, Chrome, ChromeOptions
from selenium.webdriver.common.by import By

class BusuuSpider(scrapy.Spider):
    name = 'busuu'

    def start_requests(self):
        url = 'https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home'

        settings = get_project_settings()
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.headless = True
        browser = Chrome(executable_path=settings.get('CHROME_DRIVER_PATH'),options=chrome_options)
        # browser = Firefox()

        browser.get(url)
        browser.find_element(By.XPATH, '/html/body/div[3]/main/div/div[4]/form/input[2]').send_keys("teste")
        browser.find_element(By.XPATH, '/html/body/div[3]/main/div/div[4]/form/div/input[1]').send_keys("teste")
        browser.find_element(By.XPATH, '/html/body/div[3]/main/div/div[4]/form/div/input[12]').click()
        # browser.get('https://github.com/')
        yield scrapy.Request('https://github.com/')
        browser.quit()

    def parse(self, response):
        self.log(response.xpath('/html/body/div[1]/header/div[7]/details/summary/img/@alt').extract_first())
