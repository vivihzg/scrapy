import scrapy

class QuotesSpider(scrapy.Spider):
    name = ''
    start_urls = ['https://www.projuris.com.br/blog/']

    def parse(self, response):
        titulo = response.css('h2.x-text-content-text-primary')
