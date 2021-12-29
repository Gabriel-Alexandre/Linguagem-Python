import scrapy

class InfoSpider(scrapy.Spider):

    name = "info"
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        ul = response.xpath('//ul[1]/li')
        for li in ul:
            href = li.xpath('./a/@href').extract_first()
            # O código precisa ser melhorado.
            if href and "https://www.udacity.com/course/" in href:
                # newUrl = f'https://br.udacity.com{href}'

                self.log(href)

            # yield scrapy.Request(
            #     url=newUrl,
            #     callback=self.parse_detail
            # )

    # def parse_detail(self, response):
    #     title = response.xpath('//title/text()').extract_first()
    #     headline = response.xpath(
    #         '//h2[contains(@class, "course-header-subtitle")]/text()'
    #     ).extract_first()
    #     image = response.xpath(
    #         '/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/img/@src'
    #     ).extract_first()
    #     instructors = []

    #     for div in response.xpath('//div[contains(@class, "instructor-information-entry")]'):
    #         instructors.append(
    #             {
    #                 'name': div.xpath('.//h3//span/text()').extract_first(),
    #                 'image': div.xpath('.//img/@src').extract_first(),
    #             }
    #         )

    #     yield {
    #         'title': title,
    #         'headline': headline,
    #         'image': image,
    #         'instructors': instructors,
    #     }
