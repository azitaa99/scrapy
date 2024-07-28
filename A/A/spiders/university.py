from logging import info
from turtle import position
from typing import Any
import scrapy
from scrapy.http import Response
from bs4 import BeautifulSoup
from A.items import BItem
from scrapy.loader import ItemLoader






class uniSpider(scrapy.Spider):
    name='university'


    
    start_urls=['https://research.london.ac.uk/search/staff-directory']

    
    info={}
    def parse(self, response , **kwargs):

       
        for p in response.css(".summary"):
            name=p.css('a::text').get()
            link=p.css('a::attr(href)').get()
            yield response.follow(link,self.parse_info, meta={'name':name})

        next_page=response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page,callback=self.parse)



            
   
    def parse_info(self, response):
        item=BItem()
        content=BeautifulSoup(response.text ,'html.parser')
        item['professor']=response.meta.get('name')

        
        for d in content.select('dt'):
            text=d.get_text(strip=True)
            if str(text) == "Position:":
                position = d.find_next_sibling('dd').text
                item['position']=position
         
            if str(text) == "Email address:":
                email = d.find_next_sibling('dd').find('a').text
                item['email']=email

        yield item
            

            
        

       

        
            

       
       
        
        
    