import scrapy
import pymongo
from pymongo import MongoClient
from inline_requests import inline_requests
from scrapy.selector import Selector

# if you want to store data in database
#client = pymongo.MongoClient('localhost',27017)
#db = client['<name_of_database>']

class ClassName(scrapy.Spider):
    name = "<spidername>"
    
    # handle_httpstatus_all = True
    def __init__(self, pages=None, *args, **kwargs):
        super(ClassName, self).__init__(*args, **kwargs)
        self.pages = pages.split(',')
        self.final_list = []

    def start_requests(self):
# part for handling individual request in for loop 
        for href1 in self.pages:
            yield scrapy.Request(href1,callback=self.parse)
        

    def parse(self,response):
#       here is the part for extraction in the required page
#       you can use the css selector or Xpath to extract required data's
        pass        
    
# to handle multiple parsing, or carrying links more than two for a particalur task
# we use inline request options
    
    # @ inline request        
    def parse_data(self,response):
#       this is also the part for extracting the page
        pass
        