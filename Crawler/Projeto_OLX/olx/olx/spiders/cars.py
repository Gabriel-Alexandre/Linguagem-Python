import scrapy

class CarsSpider(scrapy.Spider):

    name = "cars"
    allowed_domains = ["pe.olx.com.br/veiculos/carros"]
    start_urls = ['http://pe.olx.com.br/veiculos/carros/']

    def parse(self, response):
        items = response.xpath('//ul[@id="ad-list"]/li')
        for item in items:
            self.log(item.xpath('./a/@href').extract_first())