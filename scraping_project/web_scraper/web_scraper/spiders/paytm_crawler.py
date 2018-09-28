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
        for d in items.select('.//div/div/div/a/div/div/text()'):
            if 'Cashback' not in d.extract():
                items_name.append(d.extract())
        for d in items.select('.//div/div/div/a/div/div/div/text()'):
            items_price.append(d.extract())
        for d in items.select('.//div/div/div/a/div/img/@src'):
            items_img.append(d.extract())
        for d in items.select('.//div/div/div/a/@href'):
            items_src.append('https://www.paytmmall.com'+d.extract())
        items_list=list(zip(list(range(len(items_name))),items_name,items_price,items_src,items_img))
        #print(len(items_name),len(items_price),len(items_src),len(items_img))
        items_dict = {}
        for i in items_list:
            items_dict[i[0]]=i
        yield {'paytm' : items_dict}
