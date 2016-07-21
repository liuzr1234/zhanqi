# -*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import scrapy
from zhanqi.items import ZhanqiItem
from scrapy.selector import Selector


class ZhanqiSpider(scrapy.Spider):
    name = "zhanqi"
    allowed_domains = ["zhanqi.tv"]
    start_urls = [
        "http://www.zhanqi.tv/lives"
    ]



    def parse(self, response):
        sel = Selector(response)
        item = ZhanqiItem()


        item['actor_name'] = sel.xpath('//div[@class="meat"]/span[@class="anchor anchor-to-cut dv"]/text()').extract()
        item['program_name'] = sel.xpath('//div[@class="info-area"]/span[@class="name"]/text()').extract()
        #item['picture_url'] = sel.xpath('//div[@class="imgBox"]/img/@src').extract()


        yield item
