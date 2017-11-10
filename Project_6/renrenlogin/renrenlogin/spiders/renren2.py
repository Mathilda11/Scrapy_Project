# -*- coding: utf-8 -*-
import scrapy

# 正统模拟登录方法：
# 首先发送登录页面的get请求，获取到页面里的登陆必须的参数，比如知乎的_xsrf
# 然后和账户密码一起post到服务器，登录成功
class Renren2Spider(scrapy.Spider):
    name = "renren2"
    allowed_domains = ["renren.com"]
    start_urls = (
        'http://www.renren.com/PLogin.do',
    )

    def parse(self, response):
        # _xsrf = response.xpath('//_xsrf').extract()[0]
        yield scrapy.FormRequest.from_response(
                response,
                formdata = {'email':'18192028002','password':'950124',#,'_xsrf':_xsrf},
                    }
                callback = self.parse_page
        )
    
    def parse_page(self,response):
        print '=====1=====' + response.url
        url = 'http://www.renren.com/960909809/profile'
        yield scrapy.Request(url,callback=self.parse_newpage)

    def parse_newpage(self,response):
        print '=====2====' + response.url
        with open('myinfo1.html','w') as filename:
            filename.write(response.body)

