import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com/']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):

        request = response.follow(url='https://zhidao.baidu.com/uteam/contribute?teamId=4092', callback=self.parse_post, dont_filter=True)
        request.meta['PhantomJS'] = True
        yield request

    def parse_post(self, response):
        yield {"ask": response.css(".ask")}
