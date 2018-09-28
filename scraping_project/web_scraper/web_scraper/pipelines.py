# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from web_interface.views import tp
from web_interface.models import ScrapyItem

class WebScraperPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items=''

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
        )
    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        try:
            item = ScrapyItem.objects.get(unique_id=self.unique_id)
        except ScrapyItem.DoesNotExist:
            item=ScrapyItem()
        item.unique_id = self.unique_id
        if 'paytm' in self.items:
            item.paytm_data=self.items['paytm']
        elif 'snapdeal' in self.items:
            item.snapdeal_data=self.items['snapdeal']
        item.save()

    def process_item(self, item, spider):
        self.items=item
        return item
