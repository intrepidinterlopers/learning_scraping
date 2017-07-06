import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']
    
    def parse(self, response):
        self.log(' '.join(['URL visited:', response.url]))
        for quote in response.css('div.quote'):
            yield {'text': quote.css('span.text::text').extract_first(),
                   'author': quote.css('small.author::text').extract_first(),
                   'tags': quote.css('a.tag::text').extract()
                   }
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
