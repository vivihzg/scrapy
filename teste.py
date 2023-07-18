import scrapy
class TestSpider(scrapy.Spider):
    name = "test"

    start_urls = [
        "https://www.projuris.com.br/code/scrapy/",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)