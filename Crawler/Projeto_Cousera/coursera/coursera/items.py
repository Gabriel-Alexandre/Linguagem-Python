# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join

# Items -> Responsável por padronizar os items coletados e evitar erros.
# ItemLoader -> Responsável por padronizar como será a criação de cada item.

# -> Os dois atuando juntos cooperam para que seja coletada a informação correta.
# -> Também podem ajudar no pré-processamente de limpeza dos dados. (Apesar de ser responsabilidade do pipeline).
# -> Lembrar que eu posso customizar a captura e o retorno de cada ItemLoader.
#   - Nesse caso, só é criar uma classe ItemLoader para o item que precisa de uma captura customizada e no spider
# em vez de usar CourseraItem() para geram o ItemLoader, usar a classe customizada criada.

# Classe que representa meus items que serão gerados pelo spider.
class CourseraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # Define como os items serão armazenados.
    title = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field(
        # output_processor: Definindo como quero minha saída.
        # Junta toda lista de saída em uma grande string separada por ' | '.
        output_processor=Join(' | ')
    )
