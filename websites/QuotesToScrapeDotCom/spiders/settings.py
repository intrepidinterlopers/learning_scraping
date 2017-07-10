# coding: utf-8

BOT_NAME = 'QuotesToSpiderDotCom'

SPIDER_MODULES = ['QuotesToSpiderDotCom.spiders']
NEWSPIDER_MODULE = 'QuotesToSpiderDotCom.spiders'

# ScrapySplash settings

SPLASH_URL = 'http://localhost:8050'
DOWNLOADER_MIDDLEWARES = {'scrapy_splash.SplashCookiesMiddleware': 723,
                          'scrapy_splash.SplashMiddleware': 723,
                          'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810}
SPIDER_MIDDLEWARES = {'scrapy_splash.SplashDeduplicateArgsMiddleware': 100}
DUPEFILTER_CLASS = 'crapy_splash.SplashAwareDupeFilter'

