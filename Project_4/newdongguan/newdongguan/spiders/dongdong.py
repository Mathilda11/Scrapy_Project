# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newdongguan.items import NewdongguanItem

class DongdongSpider(CrawlSpider):
    name = 'dongdong'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    
    pagelink = LinkExtractor(allow=("type=4"))
    contentlink = LinkExtractor(allow=(r"/html/question/\d+/\d+.shtml"))
    rules = (
        Rule(pagelink, process_links = "deal_links",follow = True),
        Rule(contentlink,callback = "parse_item")
    )
    def deal_links(self,links):
        for each in links:
            each.url = each.url.replace('?','&').replace("Type&","Type?")
        return links

    def parse_item(self, response):
        print response.url
        
        item = NewdongguanItem()
        item['title'] = response.xpath('//div[contains(@class,"pagecenter p3")]//strong/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        item['url'] = response.url

        yield item
        
