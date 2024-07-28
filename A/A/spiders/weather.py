from typing import Any
import scrapy
from scrapy.http import response
from scrapy.loader import ItemLoader
from A.items import AItem



class weatherspider(scrapy.Spider):
    name='weather'
    start_urls=["https://www.accuweather.com/en/world-weather"]

    def parse(self, response: response.Response, **kwargs) :
        for country in response.css('a.nearby-location.weather-card'):
            l=ItemLoader(item=AItem(),selector=country)
            l.add_css('country','span.text.title.no-wrap::text')
            l.add_css('temp','span.text.temp::text')
            yield l.load_item()
           
            

        