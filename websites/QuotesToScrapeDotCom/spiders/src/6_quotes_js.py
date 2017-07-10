"""
Scrapy tutorial from https://learn.scrapinghub.com/scrapy/
Extracting quotes from javascript pages using scrapy and splash.
"""
import scrapy
import scrapy_splash


class QuotesSpiderJS(scrapy.Spider):
    name = 'quotes_js'
    custom_settings = {
        'SPLASH_URL': 'http://localhost:8050',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
            },
        'SPIDER_MIDDLEWARES': {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
            },
        'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
        }
    
    def start_requests(self):
        yield scrapy_splash.SplashRequest(url='http://quotes.toscrape.com/js',callback=self.parse)
        
    def parse(self, response):
        self.log(' '.join(["URL visited:", response.url]))
        for quote in response.css('div.quote'):
            item = {'author': quote.css('small.author::text').extract_first(),
                    'text': quote.css('span.text::text').extract_first(),
                    'tags': quote.css('a.tag::text').extract()
                    }
