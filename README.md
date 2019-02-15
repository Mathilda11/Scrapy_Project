# 使用Scrapy框架的爬虫项目
## Scrapy运行流程大概如下：
- 引擎从调度器中取出一个链接(URL)用于接下来的抓取
- 引擎把URL封装成一个请求(Request)传给下载器
- 下载器把资源下载下来，并封装成应答包(Response)
- 爬虫解析Response
- 解析出实体（Item）,则交给实体管道进行进一步的处理
- 解析出的是链接（URL）,则把URL交给调度器等待抓取

## 爬虫实例
1. [itcast网站教师信息爬虫](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_1)
2. [腾讯招聘网自动翻页采集](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_2)
3. [腾讯招聘网自动翻页采集(CrawlSpider版本)](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_3)
4. [阳光热线问政平台爬虫](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_4)
5. [斗鱼图片下载爬虫](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_5)
6. [人人网模拟登录](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_6)
7. [豆瓣电影top250和MongoDB数据存储](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_7)
