import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from coursera.items import CourseraItem

class CourseraSpider(scrapy.Spider):
    # Exemplo de como passar o atributo na linha de comando:
    # - scrapy crawl coursera -a category=computer-science

    name = "coursera"
    category = None

    # Executa o primeiro request.
    def start_requests(self):
        # Se nenhuma categoria for passada, acessar todas categorias.
        if self.category is None:
            yield scrapy.Request(
                url='https://www.coursera.org/browse?languages=pt',
                callback=self.parse
            )
        # Se alguma categoria for passada, acessar essa categoria.
        else:
            yield scrapy.Request(
                url='https://www.coursera.org/browse/%s' % self.category,
                callback=self.parse_category
            )
        # No mais, o código vai executar da mesma forma para as duas opções.

    # Executa como callbak de start_requests.
    def parse(self, response):
        categories = response.xpath('//div[contains(@class, "slick-slide")]/div/div/a')
        for cat in categories:
            cat_url = cat.xpath('./@href').extract_first()
            self.log('Category: %s' % cat_url)

            # Forma de adicionar os itens sem usar o ItemLoader.
            #   - Usar quando não precisar de um processamento nos items.

            # item = CourseraItem()
            # item['title'] = cat_url

            # yield item

            # Definindo meu ItemLoader.
            loader = ItemLoader(CourseraItem(), response=response)
            # Definindo seu output_processor.
            # TakeFirst(): significa que o item adicionado já está pronto para o pipeline.
            #   - Se o item adicionado precisar passar por algum outro processamento, definir no arquivo "items.py".
            loader.default_output_processor = TakeFirst()
            # Adicionando valores.
            loader.add_value('url', response.url)
            loader.add_value('title', cat_url)
            yield loader.load_item()

            # yield scrapy.Request(
            #     url='https://www.coursera.org%s' % cat_url,
            #     callback=self.parse_category
            # )
        loader = ItemLoader(CourseraItem(), response=response)
        loader.default_output_processor = TakeFirst()
        # Adicionando valores através do xpath.
        loader.add_xpath(
            'category', '//div[contains(@class, "slick-slide")]/div/div/a/@href'
        )
        # "Retornando" items gerados.
        yield loader.load_item()
    
    def parse_category(self, response):
        courses = response.xpath('//div[contains(@class, "slick-slide")]/div/div/div/div/a')
        for course in courses:
            course_url = course.xpath("./@href").extract_first()
            yield scrapy.Request(
                url='https://www.coursera.org%s' % course_url,
                callback=self.parse_course
            )
        
    def parse_course(self, response):
        item = CourseraItem()
        item['title'] = response.xpath("//h1/text()").extract_first()
        yield item
        # yield {
        #     'title': response.xpath("//h1/text()").extract_first()
        # }
