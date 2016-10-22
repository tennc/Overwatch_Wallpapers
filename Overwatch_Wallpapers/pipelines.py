#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
#from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class OverwatchWallpapersPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     return item
    # change pic other name
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-4] +'.'+ request.url.split('/')[-2]  # get pic name
        return 'full/%s' % (image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['picurl']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item




