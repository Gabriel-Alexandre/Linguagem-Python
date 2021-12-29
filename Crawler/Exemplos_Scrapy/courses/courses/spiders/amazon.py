from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Crawspider: Spider prota que serve para vários tipos de sites.
#   - Segue regras para percorrer um determinado site.
#   - Muito boa pra utilzar quando o site segue um padrão de estrutura de links.
class AmazonSpider(CrawlSpider):
    name = 'amazon'
    # allowed_domains = ['www.amazon.com.br']
    start_urls = ['https://www.amazon.com.br/']

    # O método parse já é implementado.

    # Definindo regras do meu crawspider.
    rules = (
        Rule(
            # Percorre todos os links que contém (link_base + "allow").
            LinkExtractor(
                # link completo: 'https://www.amazon.com.br/b/'
                allow='b/',
            # Cada vez que entrar em um link com essa estrutura, executar a função ("callback").
            #   - Se o ("callback") não for passado, ele vai executar a função parse, que já é implementada pela classe.
                
            ), callback='parse_product'
        # Posso criar outras regras, para que a partir de uma página acessada, outra página seja acessada e assim
        #por diante.
        # - Cada página pode ter sua própria regra e sua própria função de callback.

        # Rule(
        #     # Percorre todos os links que contém (link_base + "allow").
        #     LinkExtractor(
        #         # link completo: 'https://www.amazon.com.br/b/'
        #         allow='/b', 
        #         # Cada vez que entrar em um link com essa estrutura, executar a função ("callback").
        #         callback='parse_product'
        #     )
        ), # Lembrar de colocar essa virgula aqui, é importante para que Rule() entenda que é uma tupla.

    )

    def parse_product(self, response):
        self.log(response.xpath("//h1/text()").extract_first())

