import scrapy

# No scrapy a requisições são feitas de forma assincrona.

# Xpath: É uma linguagem de consulta para selecionar nós de um documento XML.
# - Para entender ele, vou utilizar a prática e o auxílio do google.

# Spider
class UdacitySpider(scrapy.Spider):
    # Nome do spider
    name = "udacity"
    # Lista de links a serem pencorridos.
    start_urls = ['https://br.udacity.com/courses/all/']

    # Função que executa na primeira requisição.
    # - Posso retorna um item ou uma nova requisição.
    def parse(self, response):
        divs = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div")
        for div in divs:
            link = div.xpath('.//h3/a')
            title = link.xpath('./text()').extract_first()
            href = link.xpath('./@href').extract_first()
            img = div.xpath('.//img[contains(@class, "img-responsive")]/@src').extract_first()
            description = div.xpath('.//div[2]/div[2]/text()').extract_first()
            # Gerador - Retorna os valores da lista de recebida (start_urls), de forma parcial.
            yield {
                'title': title,
                'url': href,
                'image': img,
                'description': description,
            }

# -> Por algum motivo, quando eu executo: "scrapy runspider (nome_spider).py -o (nome_spider).csv/json/etc", o arquivo
# não é escrito corretamente.
