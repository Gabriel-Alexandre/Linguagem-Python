import scrapy


class BusuuSpider(scrapy.Spider):
    name = 'busuu'
    start_urls = ['https://www.busuu.com/pt/hello']

    def parse(self, response):
        self.log(response.xpath('/html/body/div[2]/div[1]/header/nav/div/div/div[2]/a/@href').extract_first())
