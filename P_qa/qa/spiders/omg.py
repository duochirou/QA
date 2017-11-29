import scrapy
import json
from qa.items import BaiduItem
class BaiduSpider(scrapy.Spider):
    name = 'omg'
    allowed_domains = ['baidu.com/']
    # 拼接字符串
    urls = []
    for pn in range(0, 190150, 50):
        # type = 1 : 被采纳
        url = 'https://zhidao.baidu.com/uteam/ajax/answer?teamId=4092&pn=%d&rn=50'%(pn)
        urls.append(url)
    start_urls = urls

    # test
    #start_urls = ['https://zhidao.baidu.com/uteam/ajax/answer?teamId=4092&pn=0&rn=50&type=1',]

    def parse(self, response):
        bodyStr = response.body.decode()
        bodyJson = json.loads(bodyStr)
        # 'errno': 0, 'errmsg': '操作成功~', 'data':{}
        if bodyJson['errno'] == 0:
            print("gogogogogogo-------------------------------------")
        if 'data' in bodyJson:
            print(type(bodyJson['data']))
            #{'monthlyTotalWealth': 266664, 'monthlyAnswerUserNum': 679,
            # 'monthlyAnswerList':
            data = bodyJson['data']
            monthlyTotalWealth = data['monthlyTotalWealth']
            monthlyAnswerUserNum = data['monthlyAnswerUserNum']
            monthlyAnswerList = data['monthlyAnswerList']
            # item  dict_keys(['qid', 'qtitle', 'qUName', 'qUid', 'qTime', 'rid',
            # 'rTime', 'rUName', 'rContent', 'rUid', 'isGood', 'time', 'rAuthentic', 'imId'])
            for element in monthlyAnswerList:
                item = BaiduItem()
                item['qid'] = element['qid']
                item['qtitle'] = element['qtitle']
                item['rContent'] = element['rContent']
                item['isGood'] = element['isGood']
                yield item
