# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class ImagesPipeline(ImagesPipeline):
    # 获取settings文件里设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imageLink"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["nickName"] + ".jpg")
        item["imagePath"] = self.IMAGES_STORE + "/" + item["nickName"]
        return item

