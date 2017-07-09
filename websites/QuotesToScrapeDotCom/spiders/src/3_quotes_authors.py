"""
Scrapy tutorial from https://learn.scrapinghub.com/scrapy/
Extracting author info by following hyperlinks.
"""
import scrapy
            
            
class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com']
    
    def parse(self, response):
        self.log(' '.join(["URL visited:", response.url]))
        author_urls = response.css('div.quote > span > a::attr(href)').extract()
        for url in author_urls:
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_details)
            
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            
    def parse_details(self, response):
        self.log(' '.join(["URL visited (details):", response.url]))
        yield {'author': response.css('h3.author-title::text').extract_first().rstrip(),
               'born': response.css('span.author-born-date::text').extract_first(),
               'place': response.css('span.author-born-location::text').extract_first().lstrip('in '),
               'description': response.css('div.author-description::text').extract_first().strip()
               }
               
        
            
        
