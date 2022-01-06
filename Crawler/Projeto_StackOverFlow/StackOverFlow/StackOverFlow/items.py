# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join


class StackoverflowItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    votes = scrapy.Field()
    responses = scrapy.Field()
    person = scrapy.Field()
    tags = scrapy.Field(
        output_processor=Join('/')
    )
