import scrapy

class CarsSpider(scrapy.Spider):

    name = "cars"
    allowed_domains = ["pe.olx.com.br"]
    start_urls = ['http://pe.olx.com.br/veiculos/carros/']

    def parse(self, response):
        items = response.xpath(
            '//ul[@id="ad-list"]/li'
        )
        # for item in items:
        #     self.log(item.xpath('./a/@href').extract_first())
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            # Não fazer requisições para páginas inválidas
            if url != None:
                yield scrapy.Request(url=url, callback=self.parse_detail)

        # Capturando link para a próxima página.
        next_page = response.xpath(
            '//div[contains(@class, "sc-hmzhuo kJjuHR sc-jTzLTM iwtnNi")]/a/@href'
        )

        # Se ainda tiver página, fazer uma nova requisição.
        # if next_page:
        #     self.log('Próxima Página: {}'.format(next_page.extract_first()))
        #     yield scrapy.Request(
        #         url=next_page.extract_first(), callback=self.parse
        #     )

    def parse_detail(self, response):
        title = response.xpath('//h1/text()').extract_first()
        # following-sibling::(tipo tag) -> pega a tag que está no mesmo nível.
        cat = response.xpath(
            '//span[contains(text(), "Categoria")]/following-sibling::a/text()'
        ).extract_first()
        modelo = response.xpath(
            '//span[contains(text(), "Modelo")]/following-sibling::a/text()'
        ).extract_first()
        marca = response.xpath(
            '//span[contains(text(), "Marca")]/following-sibling::a/text()'
        ).extract_first()
        year = response.xpath(
            '//span[contains(text(), "Ano")]/following-sibling::a/text()'
        ).extract_first()
        tipo_veiculo = response.xpath(
            '//span[contains(text(), "Tipo de veículo")]/following-sibling::span/text()'
        ).extract_first()
        cor = response.xpath(
            '//span[contains(text(), "Cor")]/following-sibling::span/text()'
        ).extract_first()

        yield {
            'titulo': title,
            'categoria': cat,
            'modelo': modelo,
            'marca': marca,
            'ano': year, 
            'tipoVeiculo': tipo_veiculo,
            'cor': cor
        }
