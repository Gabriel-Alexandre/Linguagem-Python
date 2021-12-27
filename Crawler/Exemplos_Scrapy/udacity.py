# import scrapy

# # No scrapy a requisições são feitas de forma assincrona.

# # Xpath: É uma linguagem de consulta para selecionar nós de um documento XML.
# # - Para entender ele, vou utilizar a prática e o auxílio do google.

# # Spider
# class UdacitySpider(scrapy.Spider):
#     # Nome do spider
#     name = "udacity"
#     # Lista de links a serem pencorridos.
#     start_urls = ['https://br.udacity.com/courses/all/']

#     # Função que executa na primeira requisição.
#     # - Posso retorna um item ou uma nova requisição.
#     def parse(self, response):
#         divs = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div")
#         for div in divs:
#             link = div.xpath('.//h3/a')
#             title = link.xpath('./text()').extract_first()
#             href = link.xpath('./@href').extract_first()
#             img = div.xpath('.//img[contains(@class, "img-responsive")]/@src').extract_first()
#             description = div.xpath('.//div[2]/div[2]/text()').extract_first()
#             # Gerador - Retorna os valores da lista de recebida (start_urls), de forma parcial.
#             yield {
#                 'title': title,
#                 'url': href,
#                 'image': img,
#                 'description': description,
#             }

# # -> Por algum motivo, quando eu executo: "scrapy runspider (nome_spider).py -o (nome_spider).csv/json/etc", o arquivo
# # não é escrito corretamente.

import scrapy

class UdacitySpider(scrapy.Spider):

    name = "udacity"
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div")
        for div in divs:
            link = div.xpath('.//h3/a')
            href = link.xpath('./@href').extract_first()
            # Retornando uma nova requisição.
            yield scrapy.Request(
                url='https://br.udacity.com%s' % href,
                callback=self.parse_detail
            )

    def parse_detail(self, response):
        # Extraindo items necessários e retornando items.
        title = response.xpath('//title/text()').extract_first()
        headline = response.xpath(
            '//h2[contains(@class, "course-header-subtitle")]/text()'
        ).extract_first()
        image = response.xpath(
            '/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/img/@src'
        ).extract_first()
        instructors = []
        for div in response.xpath('//div[contains(@class, "instructor-information-entry")]'):
            instructors.append(
                {
                    'name': div.xpath('.//h3//span/text()').extract_first(),
                    'image': div.xpath('.//img/@src').extract_first(),
                }
            )
        yield {
            'title': title,
            'headline': headline,
            'image': image,
            'instructors': instructors,
        }
