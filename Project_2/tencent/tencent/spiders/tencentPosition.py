# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]

    url = "http://hr.tencent.com/position.php?&start="
    offset = 0

    start_urls = [url + str(offset)]
    

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()

            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]

            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]

            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]

            item['positionNum'] = each.xpath("./td[3]/text()").extract()[0]

            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            
            
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.offset < 2400:
            self.offset += 10

        # 每次处理完一页数据后，重新发送下一页数据请求
        # 自增10。
        yield scrapy.Request(self.url + str(self.offset),callback = self.parse)

