import scrapy
from scrapy_selenium import SeleniumRequest


class InfoSpider(scrapy.Spider):
    name = 'info'
    start_urls = ['https://github.com/login/']

    def parse(self, response):
        url='https://github.com/login/'
        yield SeleniumRequest(url=url, callback=self.parse_result)

    def parse_result(self, response):
        self.log(response.xpath("/html/body/div[3]/main/div/div[1]/h1/text()").extract_first())