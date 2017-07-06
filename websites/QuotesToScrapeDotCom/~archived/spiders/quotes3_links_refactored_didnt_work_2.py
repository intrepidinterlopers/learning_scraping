import scrapy
"""
This didn't work either. Maybe nested functions.
"""

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']
    
    def parse(self, response):
        self.log(' '.join(["URL visited:", response.url]))
        for quote in response.css('div.quote'):
            item = {'author': quote.css('small.author::text').extract_first(),
                    'name': quote.css('span.text::text').extract_first(),
                    'tags': quote.css('a.tag::text').extract()
                    }
            author_url = response.urljoin(quote.css('span > a::attr(href)').extract_first())
            # item['author info'] =
            
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            
    def parse_author(self, url, response):
        scrapy.Request(url=url, callback=self.parse_author)
        return {'birth date': response.css('span.author-born-date::text').extract_first(),
               'birth place': response.css('span.author-birth-location::text').extract_first(),
               'description': response.css('div.author-description::text').extract_first()
              }
        
        
        
    
