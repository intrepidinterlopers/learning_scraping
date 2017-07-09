"""
Scrapy tutorial from https://learn.scrapinghub.com/scrapy/
Extracting all quotes from infinite scrolling web pages.
"""
import json
import scrapy


class QuotesInfSpider(scrapy.Spider):
    name = 'quotes_inf'
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]
    
    def parse(self, response):
        self.log(' '.join(["URL visited:", response.url]))
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {"author": quote['author']['name'],
                   'quote': quote['text'],
                   'tags': quote['tags']
                   }
            if data['has_next']:
                next_page = data['page'] + 1
                yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)
