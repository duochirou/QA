# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class QaPipeline(object):
    def process_item(self, item, spider):
        return item

# class JsonWriterPipeline(object):
#
#     def open_spider(self, spider):
#         self.file = codecs.open('items.json', 'wb', encoding='utf-8')
#
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line.decode("unicode_escape"))
#         return item
class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items_solved.jl', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
