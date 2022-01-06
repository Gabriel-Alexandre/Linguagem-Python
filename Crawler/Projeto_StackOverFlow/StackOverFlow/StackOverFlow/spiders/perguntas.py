import scrapy
from StackOverFlow.items import StackoverflowItem


class PerguntasSpider(scrapy.Spider):
    name = 'perguntas'
    allowed_domains = ['pt.stackoverflow.com']
    start_urls = ['https://pt.stackoverflow.com/questions']
    number_pag = None

    def parse(self, response):
        questions = response.xpath('//div[contains(@class, "question-summary")]')

        self.log(len(questions))

        for question in questions:
            item = StackoverflowItem()
            item['title'] = question.xpath('./div[2]/h3/a/text()').extract_first()
            item['description'] = question.xpath('./div[2]/div/text()').extract_first()
            item['votes'] = question.xpath('./div[1]/div/div[1]/div/span/strong/text()').extract_first()
            item['responses'] = question.xpath('./div[1]/div/div[2]/strong/text()').extract_first()
            item['person'] = question.xpath('./div[2]/div[2]/div[2]/div/div[3]/a/text()').extract_first()
            item['tags'] = question.xpath('./div[2]/div[2]/div[1]/div/a/text()').extract()

            yield item

        if self.number_pag is not None:
            for c in range(int(self.number_pag)):
                url_callback = f"{'https://pt.stackoverflow.com'}{response.xpath('/html/body/div[3]/div[2]/div[1]/div[5]/a[6]/@href').extract_first()}"
                yield scrapy.Request(
                    url=url_callback,
                    callback=self.parse
                )