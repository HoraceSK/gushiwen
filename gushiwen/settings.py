# -*- coding: utf-8 -*-

# Scrapy settings for gushiwen project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'gushiwen'

SPIDER_MODULES = ['gushiwen.spiders']
NEWSPIDER_MODULE = 'gushiwen.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/74.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 8
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate',
    # 'Accept-Language':'en-GB,en;q=0.5',
    # 'Cache-Control':'max-age=0',
    # 'Connection':'keep-alive',
    # 'DNT':1,
    # 'Host':'www.shicimingju.com',
    # 'Referer':'http://www.baidu.com',
    # 'Upgrade-Insecure-Requests':1,
    # 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
# }
DEFAULT_REQUEST_HEADERS ={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-GB,en;q=0.5',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1592893092,1592893105,1592893983,1592894643; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1592894643; ASP.NET_SessionId=pdsnehm4uxoeggvxvfaccowl; codeyzgswso=29db9dfd25f0be7e; login=flase',
    'DNT':1,
    'Host':'so.gushiwen.cn',
    'Referer':'https://www.gushiwen.cn/',
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'gushiwen.middlewares.GushiwenSpiderMiddleware': 543,
    # 'gushiwen.middlewares.FakeHeaderMiddleware': 543,
    # 'gushiwen.middlewares.ProxyIPMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'gushiwen.middlewares.GushiwenDownloaderMiddleware': 543,
    'gushiwen.middlewares.FakeHeaderMiddleware': 543,
    'gushiwen.middlewares.ProxyIPMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'gushiwen.pipelines.GushiwenPipeline': 300,
    'gushiwen.pipelines.ShijingScanPipeline': 300,
    'gushiwen.pipelines.ShijingSinglePipeline': 300,
    'gushiwen.pipelines.YemengdePipeline': 300,
    'gushiwen.pipelines.ShiciByAuthorPipeline': 300,
    # 'gushiwen.pipelines.ShiciByMarkPipeline': 300,
    'gushiwen.pipelines.ShijingSCMJPipeline': 300,
    'gushiwen.pipelines.GushiwenwangPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
