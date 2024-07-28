from gc import callbacks
from typing import Any
import scrapy
from scrapy.http import Response




class githubSpider(scrapy.Spider):
    name='github'
    start_urls=['https://github.com/login',]
     
    def parse(self, response, **kwargs):
        data={'login':'tahbazazita@gmail.com',
              'password':'testpassword'}
   
        return scrapy.FormRequest.from_response(response,url='https://github.com/session',
                    formdata=data,
                    callback=self.after_login)      
    def after_login(self, response):
        yield response.follow('https://github.com/azitaa99', self.profile)

    def profile(self,response):
        yield{'info':response.css('body > div.logged-in.env-production.page-responsive.page-profile.mine > div.application-main > main > div > div > div.Layout-sidebar > div > div > div.d-flex.flex-column > div.js-profile-editable-area.d-flex.flex-column.d-md-block > ul > li:nth-child(2) > a::text').get()}