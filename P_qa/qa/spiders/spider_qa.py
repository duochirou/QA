import scrapy
from qa.items import QaItem


class SpiderQaSpider(scrapy.Spider):
    name = 'spider_qa'
    allowed_domains = ['5ask.cn']
    start_urls = ['http://www.5ask.cn/ask/c.asp?id=minshileifalvshiwu&QType=jie',
                  'http://www.5ask.cn/ask/c.asp?id=xingshixingzhengfalvshiwu&QType=jie',
                  'http://www.5ask.cn/ask/c.asp?id=jingjileifalvshiwu&QType=jie',
                  'http://www.5ask.cn/ask/c.asp?id=jingjileifalvshiwu&QType=jie',
                  'http://www.5ask.cn/ask/c.asp?id=gongsizhuanxiangfalvfuwu&QType=jie',
                  'http://www.5ask.cn/ask/c.asp?id=qitafeisongfalvshiwu&QType=jie',]

    def parse(self, response):
        # 
        for href in response.css('p.wt a::attr(href)'):
            yield response.follow(href, self.parse_qa)

        # ��ȡ��һҳ������scrapy��������
        url_head = "http://www.5ask.cn"
        current_url = response.css(".center .on::attr(href)").extract_first()
        next_url = response.css(".center .page li:last-child a::attr(href)").extract_first()
        print("next", next_url, "current", current_url)
        if next_url != current_url:
            print("go next")
            yield response.follow(url=next_url, callback=self.parse)


    def parse_qa(self, response):
        self.logger.info("Visited %s", response.url)

        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        item = QaItem()
        item['tags'] = response.css("#SHead p a::text").extract()
        item['title'] = response.css("#QBox .qt::text").extract_first()
        item['question'] = response.css("#QBox .qcon::text").extract_first()
        item['answer'] = response.css(".lxt_list .hfnr::text").extract()
        if item['answer'] == "":
            item['answer'] = response.css(".hdcon::text").extract()
        item['url'] = response.url
        yield item

