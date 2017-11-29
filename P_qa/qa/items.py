
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tags = scrapy.Field()
    title = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()
    url = scrapy.Field()
class BaiduItem(scrapy.Item):
    # item  dict_keys(['qid', 'qtitle', 'qUName', 'qUid', 'qTime', 'rid',
    # 'rTime', 'rUName', 'rContent', 'rUid', 'isGood', 'time', 'rAuthentic', 'imId'])
    qid = scrapy.Field()
    qtitle = scrapy.Field()
    rContent = scrapy.Field()
    isGood = scrapy.Field()
