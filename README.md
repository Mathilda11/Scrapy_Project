## 🎠Scrapy框架的主要组件
- 引擎（scrapy engine）：负责调度器、下载器、爬虫、管道等各个部分的通讯，信息、信号、数据等的传递，是框架的核心
- 调度器（scheduler）：负责接收引擎发过来的URL，压入队列中，并在引擎再次请求的时候返回
- 下载器（downloader）：负责下载引擎发送的所有requests请求，并将其获取到的responses交还给引擎，由引擎交到爬虫处理
- 爬虫（spiders）：处理获取到的所有responses，从中分析提取实体item，并将还需要进一步处理的url提交给引擎
- 管道（itemPipline）：负责对爬虫爬取到的数据进一步处理，并对其进行持久化存储
- 下载中间件（downloader Middewares）：位于引擎和下载器之间的框架，主要是处理引擎与下载器之间的请求及响应
- 爬虫中间件（spider Middewares）：位于引擎和爬虫之间的框架，主要工作是处理引擎和爬虫之间的请求和响应
- 调度中间件(Scheduler Middewares)：位于引擎和调度之间的中间件，处理引擎和调度器之间请求和响应

## 🐥Scrapy运行流程
- 引擎从调度器中取出一个链接(URL)用于接下来的抓取
- 引擎把URL封装成一个请求(Request)传给下载器
- 下载器把资源下载下来，并封装成应答包(Response)
- 爬虫解析Response
- 解析出实体（Item），则交给管道进行进一步的处理
- 解析出的是链接（URL），则把URL交给调度器等待抓取

## 🐟爬虫实例
1. [itcast网站教师信息爬虫](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_1)
2. [腾讯招聘网自动翻页采集](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_2)
3. [腾讯招聘网自动翻页采集(CrawlSpider版本)](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_3)
4. [阳光热线问政平台爬虫](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_4)
5. [斗鱼图片下载爬虫](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_5)
6. [人人网模拟登录](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_6)
7. [豆瓣电影top250和MongoDB数据存储](https://github.com/Mathilda11/Scrapy_Project/tree/master/Project_7)
