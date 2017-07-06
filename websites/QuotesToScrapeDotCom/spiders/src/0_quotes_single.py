import scrapy
import json
from pprint import pprint


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["http://quotes.toscrape.com/random"]
    
    def parse(self, response):
        self.log(' '.join(["URL Visited:", response.url]))
        quote_data = {'author': response.css('small.author::text').extract_first(),
                      'text': response.css('span.text::text').extract_first()[1: -1],
                      'tag': response.css('a.tag::text').extract()
                      }
        pprint(quote_data)
        yield quote_data

        
def write_quote(quote_data):
    with open('item.json', 'a') as write_obj:
        write_obj.write(str(quote_data))
        
        
# if __name__ == '__main__'
    # print('main()', '=' * 50)
    # spider1 = QuotesSpider()
    # scrapy.Spider.
    # write_quote(next(QuotesSpider.parse(QuotesSpider)))
