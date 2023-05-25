import scrapy

# create a class to scrape somethign specific
class QuoteSpider(scrapy.Spider) :
    name = 'quotes'
    # name of what we are looking for
    start_urls = [
        'https://quotes.toscrape.com'
        ]
    # the urls that we are scrapping can do multiples

    # create a method to look for what we are scrapping
    def parse(self, response):
        title = response.css('title').extract()
        # response contains the source code
        # can specify what tag we are looking for in this case it is the title tag
        yield {'titletext' : title}
        # yield requires a dictionary