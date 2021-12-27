import scrapy


class CourseraSpider(scrapy.Spider):
    # nome do spider
    name = 'coursera'
    # urls executadas inicialmente
    start_urls = ['http://https://www.coursera.org/browse?languages=pt/']

    # Função que executa na primeira requisição
    def parse(self, response):
        pass
