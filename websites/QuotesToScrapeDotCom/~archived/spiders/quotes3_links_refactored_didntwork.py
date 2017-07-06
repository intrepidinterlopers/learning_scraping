import scrapy
"""
This didn't work. Maybe nested functions.
"""

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']
    
    def page(self, response):
        for quote in response.css('div.quote'):
            yield {'author': quote.css('small.author::text').extract_first(),
                   'name': quote.css('span.text::text').extract_first(),
                   'tags': quote.css('a.tag::text').extract()
                   }
        
    def next_page(self, response):
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        
    def parse(self, response):
        self.log(' '.join(["URL visited:", response.url]))
        page = self.page(response=response)
        next_page = self.next_page(response=response)
