# Define your item pipelines here
# Places the information scrapped into a database in this py file
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyprojectPipeline:
    def process_item(self, item, spider):
        return item
