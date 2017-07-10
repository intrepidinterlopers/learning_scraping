"""
Scrapy tutorial from https://learn.scrapinghub.com/scrapy/
Extracting all the quotes on a page.
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        self.log(' '.join(["URL visited:", response.url]))
        for quote in response.css('div.quote'):
            item = {'author': quote.css('small.author::text').extract_first(),
                    'text': quote.css('span.text::text').extract_first(),
                    'tags': quote.css('a.tag::text').extract()
                   }
            yield item
