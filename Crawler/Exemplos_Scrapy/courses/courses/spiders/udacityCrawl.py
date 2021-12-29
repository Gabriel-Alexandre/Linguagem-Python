from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class InfoSpider(CrawlSpider):
    name = "udacityCrawl"
    start_urls = ['https://br.udacity.com/courses/all/']

    rules = (
        Rule(
            LinkExtractor(allow='course/'), 
            callback='parse_info'),
    )

    def parse_info(self, response):
        self.log(response)

