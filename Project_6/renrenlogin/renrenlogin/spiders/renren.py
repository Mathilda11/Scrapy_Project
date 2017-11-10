# -*- coding: utf-8 -*-
import scrapy

# 实在没办法了，可以用这种方法模拟登录，麻烦一点，成功率100%

class RenrenSpider(scrapy.Spider):
    name = "renren"
    allowed_domains = ["renren.com"]
    start_urls = (
        'http://www.renren.com/xxxxx',
        'http://www.renren.com/11111',
        'http://www.renren.com/xxx',
    )

    cookies = {
	"anonymid" : "j9kycixgxap9nh",
	"_r01_" : "1",
	"Hm_lvt_966bff0a868cd407a416b4e3993b9dc8" : "1509784981",
	"_ga" : "GA1.2.1145761238.1509784981",
	"_ga" : "GA1.3.1145761238.1509784981",
	"depovince" : "GW",
	"jebe_key" : "e6c002ff-e007-4187-a9ac-32df36861914%7C5006b51af4ef7a1684b714f54d4092e1%7C1509784124238%7C1%7C1510213198749",
	"JSESSIONID" : "abcNbSzwpxxCY9UsEUF_v",
	"ch_id" : "10016",
	"wp_fold" : "0",
	"jebecookies" : "b753eb17-d437-43c5-9062-2c8f0d3b5ff2|||||",
	"ick_login" : "d56bfddd-a831-4915-b562-4ca0bb4da3e6",
	"_de" : "F9A3A36BEDD8DDAE429AFF14B6C00B65",
	"p" : "0627a933351b3700002ffc88358d39e29",
	"first_login_flag" : "1",
	"ln_uact" : "18192028002",
	"ln_hurl" : "http://head.xiaonei.com/photos/0/0/men_main.gif",
	"t" : "3b7b828006181782a5c970e5c67723ba9",
	"societyguester" : "3b7b828006181782a5c970e5c67723ba9",
	"id" : "960909809",
	"xnsid" : "602c39b7",
	"loginfrom" : "syshome",
        }
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url,cookies = self.cookies,callback=self.parse_page)

    def parse_page(self,response):
        print '=========='+response.url
        with open("ckinfo.html","w") as filename:
            filename.write(response.body)
