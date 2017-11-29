import scrapy
import json

class BaiduSpider(scrapy.Spider):
    name = 'omg'
    allowed_domains = ['baidu.com/']
    # 拼接字符串
    # urls = []
    # for pn in range(0, 190150, 50):
    #     url = 'https://zhidao.baidu.com/uteam/ajax/answer?teamId=4092&pn=%d&rn=50&type=1'%(pn)
    #     urls.append(url)
    # start_urls = urls
    start_urls = ['https://zhidao.baidu.com/uteam/ajax/answer?teamId=4092&pn=0&rn=50&type=1',]

    def parse(self, response):
        #"gbk", "ignore"
        commentsStr = response.body.decode()
        commentsJson = json.loads(commentsStr)
        print(type(commentsJson))
        yield commentsJson
