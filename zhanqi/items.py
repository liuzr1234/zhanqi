# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhanqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    actor_name = scrapy.Field()#主播名字

    program_name = scrapy.Field()#节目名字
    live_time = scrapy.Field()#直播时间
    picture_url = scrapy.Field()#节目配图