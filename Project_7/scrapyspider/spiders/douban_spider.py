#coding=utf-8
from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import DoubanMovieItem

class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
   }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)
     
    def parse(self, response):
        
        item = DoubanMovieItem()
        movies = response.xpath("//div[@class='info']")

        for each in movies:
            # 标题
            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # 信息
            item['bd'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
            # 评分
            item['star'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            # 简介
            quote = each.xpath(".//p[@class='quote']/span/text()").extract()
            if len(quote) != 0:
                item['quote'] = quote[0]
            yield item
        
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)
        
