# -*- coding: utf-8 -*-
import scrapy

class SnapdealCrawlerSpider(scrapy.Spider):
    name = 'snapdeal_crawler'

    def __init__(self, *args, **kwargs):
        self.search_data = kwargs.get('search_data')
        self.start_urls=["https://www.snapdeal.com/search?keyword="+self.search_data+"&sort=rlvncy"]

    def parse(self,response):
        items=response.xpath('//*[@id="products"]')
        items_name,items_src,items_img,items_price=([] for i in range(4))
        for d in items.select('//div/div/a/p/text()'):
            items_name.append(d.extract())
        for d in items.select('//div/a/@href'):
            if self.search_data.split()[0] in d.extract():
                items_src.append(d.extract())
        for d in items.select('//div/a/picture/source/@srcset'):
            items_img.append(d.extract())
        for d in items.select('//div/div/a/div/div/span[@class="lfloat product-price"]/text()'):
            items_price.append(d.extract())

        items_list=list(zip(list(range(len(items_name))),items_name,items_price,items_src[:len(items_name)],items_img))
        items_dict = {}
        for i in items_list:
            items_dict[i[0]]=i
        yield {'snapdeal' : items_dict}
