"""
Scrapy tutorial from https://learn.scrapinghub.com/scrapy/
Extracting quotes by filling form to login.
"""
import scrapy


class QuotesFormFillSpider(scrapy.Spider):
    name = 'quotes_form'
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]
    
    def parse(self, response):
        login_info = {'csrf_token': response.css('input[name="csrf_token"]::attr(value)').extract_first(),
                      'username': 'abc',
                      'password': 'abc'
                      }
        yield scrapy.FormRequest(url=self.login_url, formdata=login_info, callback=self.parse_quotes)
        
    def parse_quotes(self, response):
        for quote in response.css('div.quote'):
            yield {'text': quote.css('span.text::text').extract_first(),
                   'author': quote.css('span > small.author::text').extract_first(),
                   'tags': quote.css('div.tags > a::text').extract(),
                   'tag_links': {tag: response.urljoin(url) for tag, url in
                                 zip(quote.css('div.tags > a::text').extract(),
                                     quote.css('div.tags > a::attr(href)').extract()
                                     )
                                 },
                   'author_link': response.urljoin(quote.css('span > a::attr(href)').extract_first()),
                   'goodreads_link': response.urljoin(quote.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first())
                   }
