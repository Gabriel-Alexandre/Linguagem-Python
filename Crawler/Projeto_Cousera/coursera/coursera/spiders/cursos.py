import scrapy


class CourseraSpider(scrapy.Spider):
    # - O site foi atualizado, então o código precisa ser atualizado.
    # - Porém, o código ainda é válido para aprender o conteúdo.

    # exemplo de como passar o atributo na linha de comando:
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
            yield scrapy.Request(
                url='https://www.coursera.org%s' % cat_url,
                callback=self.parse_category
            )
    
    # Falta encontrar as categorias
    def parse_category(self, response):
        courses = response.xpath("//a[contains(@class, 'rc-OfferingCard')]")
        for course in courses:
            course_url = course.xpath("./@href").extract_first()
            yield scrapy.Request(
                url='https://www.coursera.org%s' % course_url,
                callback=self.parse_course
            )
        
    def parse_course(self, response):
        yield {
            'title': response.xpath("//title/text()").extract_first()
        }
