# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WaterdatascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    station = scrapy.Field()
    time = scrapy.Field()
    water_level = scrapy.Field()
    flow_rate = scrapy.Field()
    pass
