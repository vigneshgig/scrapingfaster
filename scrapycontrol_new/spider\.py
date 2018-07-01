import scrapy
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['databasename']

class classname(scrapy.Spider):
    name = 'spidername'
    def __init__(self, *args, **kwargs):
        with open('/path/to/textfile/scrapydomain.txt','r') as f:
            pages = f.read()
        self.pages = pages.split(',')
        print(self.pages)
    def start_requests(self):
        for href1 in self.pages:
            yield scrapy.Request(href1,callback=self.parse)

    def parse(self,response):
	pass
	# your extraction code
    def parse_data(self,response):
     	# your extraction code
	pass
