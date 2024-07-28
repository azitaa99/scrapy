# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import MapCompose,TakeFirst



def to_strip(value):
    return value.strip()


class AItem(scrapy.Item):
    country=scrapy.Field(output_processor=TakeFirst())
    temp=scrapy.Field(output_processor=TakeFirst())
    
class BItem(scrapy.Item):
    professor=scrapy.Field()
    position=scrapy.Field()
    email=scrapy.Field()