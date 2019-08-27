# -*- coding: utf-8 -*-
import scrapy

class PaytmCrawlerSpider(scrapy.Spider):
    name = 'paytm_crawler'

    def __init__(self, *args, **kwargs):
        self.search_data = kwargs.get('search_data')
        self.start_urls=['https://paytmmall.com/shop/search?q='+self.search_data+'&from=organic&child_site_id=6&site_id=2&category=66781']

    def parse(self, response):
        items=response.xpath('//*[@id="app"]/div/div[3]/div/div/div[3]/div[2]')
        items_name,items_src,items_img,items_price=([] for i in range(4))
        for d in items.xpath('.//div/div/div/a/div/div/text()').getall():
            if d!='Cashback':
                items_name.append(d)
        for d in items.xpath('.//div/div/div/a/div/div/div/text()').getall():
            items_price.append(d)
        for d in items.xpath('.//div/div/div/a/div/img/@src').getall():
            items_img.append(d)
        for d in items.xpath('.//div/div/div/a/@href').getall():
            items_src.append('https://www.paytmmall.com'+d)
        items_list=list(zip(list(range(len(items_name))),items_name,items_price,items_src,items_img))
        print(len(items_name),len(items_price),len(items_src),len(items_img))
        items_dict = {}
        for i in items_list:
            items_dict[i[0]]=i
        yield {'paytm' : items_dict}
