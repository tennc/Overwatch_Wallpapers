#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from Overwatch_Wallpapers.items import OverwatchWallpapersItem


class OverwatchSpider(scrapy.Spider):
    name = "overwatch"
    allowed_domains = ["wall.alphacoders.com"]
    start_urls = (
        'https://wall.alphacoders.com/by_sub_category.php?id=229118&name=Overwatch+Wallpapers&page=1',
    )

    def parse(self, response):
        for i in response.xpath('//span[@title="Download Wallpaper!"]'):
            item = OverwatchWallpapersItem()
            item['picname'] = i.xpath('@data-href').extract()[0].split('/')[-4] + '.' + \
                              i.xpath('@data-href').extract()[0].split('/')[-2]
            item['picurl'] = [i.xpath('@data-href').extract()[0]]
            yield item

        next_page = response.xpath('//a[@id="next_page"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
