#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OverwatchWallpapersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    picname = scrapy.Field()
    picurl = scrapy.Field()
    image_paths = scrapy.Field()
